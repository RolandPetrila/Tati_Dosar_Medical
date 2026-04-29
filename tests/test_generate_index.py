"""Smoke test pentru scripts/generate_index.py (sursă unică query-abil).

Validează:
  - happy path: rulare main() pe proiect real → INDEX.json cu structura completă
  - structură: stats + medici + corespondenta + documente_canonice + cross_references
  - pure functions: parse_frontmatter, slug_to_titlu, strip_md_to_preview, relpath_str
  - non-destructive: OUTPUT redirected în tmp_path
"""

import json

import generate_index


def test_main_returns_zero_and_creates_index(tmp_path, monkeypatch):
    """Happy path: rulare pe proiect real → exit 0 + INDEX.json existent."""
    output_file = tmp_path / "INDEX.json"
    monkeypatch.setattr(generate_index, "OUTPUT", output_file)

    rc = generate_index.main()

    assert rc == 0
    assert output_file.exists()


def test_index_top_level_structure(tmp_path, monkeypatch):
    """INDEX.json conține toate câmpurile top-level."""
    output_file = tmp_path / "INDEX.json"
    monkeypatch.setattr(generate_index, "OUTPUT", output_file)
    generate_index.main()

    data = json.loads(output_file.read_text(encoding="utf-8"))

    required = (
        "generated_at", "version", "stats",
        "medici_oncohelp", "corespondenta", "documente_canonice",
        "documente_pentru_dashboard", "cross_references", "files_by_path",
    )
    for field in required:
        assert field in data, f"Missing top-level field: {field}"
    assert data["version"] == "1.1"


def test_stats_required_int_keys(tmp_path, monkeypatch):
    """Stats conține metricile așteptate, toate int."""
    output_file = tmp_path / "INDEX.json"
    monkeypatch.setattr(generate_index, "OUTPUT", output_file)
    generate_index.main()

    data = json.loads(output_file.read_text(encoding="utf-8"))
    s = data["stats"]
    required = (
        "total_files_indexed", "medici_oncohelp", "threaduri_gmail",
        "documente_canonice", "documente_pentru_dashboard",
    )
    for k in required:
        assert k in s
        assert isinstance(s[k], int)


def test_files_by_path_entries_have_metadata(tmp_path, monkeypatch):
    """Fiecare entry din files_by_path are type/size_kb/last_modified."""
    output_file = tmp_path / "INDEX.json"
    monkeypatch.setattr(generate_index, "OUTPUT", output_file)
    generate_index.main()

    data = json.loads(output_file.read_text(encoding="utf-8"))
    files = data["files_by_path"]
    if not files:
        return  # proiect minim
    sample_entry = next(iter(files.values()))
    assert "type" in sample_entry
    assert "size_kb" in sample_entry
    assert "last_modified" in sample_entry


def test_relpath_str_uses_forward_slashes():
    """relpath_str returnează path cu / (nu \\), pentru cross-platform JSON."""
    p = generate_index.ROOT / "Dosar_Medical" / "CONTACTE_MEDICALE.md"
    if p.exists():
        rel = generate_index.relpath_str(p)
        assert "\\" not in rel
        assert "/" in rel


def test_parse_frontmatter_with_yaml():
    """parse_frontmatter pe MD cu frontmatter valid YAML."""
    text = """---
name: test
type: project
---

body content"""
    result = generate_index.parse_frontmatter(text)
    assert result is not None
    assert result["name"] == "test"
    assert result["type"] == "project"


def test_parse_frontmatter_with_inline_list():
    """parse_frontmatter cu listă inline `[a, b, c]`."""
    text = """---
name: test
tags: [a, b, c]
---

body"""
    result = generate_index.parse_frontmatter(text)
    assert result is not None
    assert result["tags"] == ["a", "b", "c"]


def test_parse_frontmatter_returns_none_when_missing():
    """Fără frontmatter → None."""
    assert generate_index.parse_frontmatter("no frontmatter") is None
    assert generate_index.parse_frontmatter("") is None


def test_parse_yaml_block_with_yaml():
    """parse_yaml_block parsează YAML standalone."""
    text = "id: dr-test\nnume: Test Medic\nspecialitate: oncolog"
    result = generate_index.parse_yaml_block(text)
    assert result["id"] == "dr-test"
    assert result["nume"] == "Test Medic"


def test_slug_to_titlu_with_date():
    """slug_to_titlu formatează data + capitalize."""
    result = generate_index.slug_to_titlu("2026-04-20_ct_torace_abdomen_pelvis")
    assert "(20.04.2026)" in result
    assert "CT" in result  # CT e în upper_words


def test_slug_to_titlu_without_date():
    """slug_to_titlu fără date prefix → fallback simplu."""
    result = generate_index.slug_to_titlu("schema_tratament")
    assert result.lower().startswith("schema")


def test_slug_to_titlu_with_special_terms():
    """Termeni medicali frecvenți (RMN/UPU/HP) → uppercase."""
    result = generate_index.slug_to_titlu("2024-05-30_upu_arad_dosar")
    assert "UPU" in result


def test_strip_md_to_preview_strips_frontmatter():
    """strip_md_to_preview elimină frontmatter + H1 + blockquotes meta."""
    md = """---
name: test
type: doc
---

# Header principal

> Notă meta intro

Conținut narativ aici despre proiect."""
    preview = generate_index.strip_md_to_preview(md, max_chars=200)
    assert "name: test" not in preview
    assert "Header principal" not in preview
    assert "Notă meta" not in preview
    assert "Conținut narativ" in preview


def test_strip_md_to_preview_truncates_at_max():
    """Preview e truncat la max_chars cu suffix `…`."""
    md = "Text foarte lung " * 100  # ~1700 chars
    preview = generate_index.strip_md_to_preview(md, max_chars=80)
    assert len(preview) <= 81  # max_chars + 1 (pentru …)
    assert preview.endswith("…")


def test_strip_md_to_preview_strips_markdown_syntax():
    """Markdown bold/italic/code/links → text plain."""
    md = "This is **bold** and *italic* with `code` and [link](http://x.com)."
    preview = generate_index.strip_md_to_preview(md, max_chars=300)
    assert "**" not in preview
    assert "`" not in preview
    assert "](" not in preview
