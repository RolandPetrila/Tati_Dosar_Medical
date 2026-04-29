"""Smoke test pentru scripts/audit_documente_sursa.py (R14 + R26).

Validează:
  - happy path: rulare main() pe Dosar_Medical/documente_sursa/ real, MD generat valid
  - regex patterns: FOLDER_PATTERN și FILE_PATTERN pe nume canonice/non-canonice
  - intermediate_artifacts: collect_intermediate_files() pe folder fictiv
  - non-destructive: OUTPUT redirected în tmp_path
"""

import json

import audit_documente_sursa
import pytest


def test_main_returns_zero_on_real_data(tmp_path, monkeypatch):
    """Happy path: rulare pe Dosar_Medical/documente_sursa/ real → exit 0."""
    if not audit_documente_sursa.DOCS.exists():
        pytest.skip("Dosar_Medical/documente_sursa/ nu există în acest checkout")

    output_file = tmp_path / "AUDIT.md"
    monkeypatch.setattr(audit_documente_sursa, "OUTPUT", output_file)

    rc = audit_documente_sursa.main()

    assert rc == 0
    assert output_file.exists()


def test_output_md_has_expected_sections(tmp_path, monkeypatch):
    """Output MD conține headerele așteptate (Stats + R14 + R26)."""
    if not audit_documente_sursa.DOCS.exists():
        pytest.skip("Dosar_Medical/documente_sursa/ nu există")

    output_file = tmp_path / "AUDIT.md"
    monkeypatch.setattr(audit_documente_sursa, "OUTPUT", output_file)
    audit_documente_sursa.main()

    md = output_file.read_text(encoding="utf-8")
    assert "AUDIT documente_sursa/" in md
    assert "## Stats" in md
    assert "Coverage R14 total" in md
    assert "Foldere goale > 30 zile" in md
    assert "Foldere cu nume non-canonic" in md


def test_audit_returns_dict_with_required_fields():
    """audit() returnează dict cu structura completă (chiar pe folder gol)."""
    if not audit_documente_sursa.DOCS.exists():
        pytest.skip("Dosar_Medical/documente_sursa/ nu există")

    issues = audit_documente_sursa.audit()
    assert issues is not None
    for k in ("empty_folders_long", "non_canonical_folder", "non_canonical_file",
              "missing_meta_json", "stats"):
        assert k in issues, f"Missing key: {k}"

    s = issues["stats"]
    for k in ("total_folders", "populated", "total_files", "with_meta",
              "intermediate_artifacts"):
        assert k in s, f"Missing stats key: {k}"
        assert isinstance(s[k], int)


def test_folder_pattern_matches_canonical():
    """FOLDER_PATTERN acceptă formate canonice NN_categorie."""
    p = audit_documente_sursa.FOLDER_PATTERN
    assert p.match("01_identitate")
    assert p.match("12_biopsie_2026")
    assert p.match("99_altele")
    assert p.match("14_UPU_2024_05_30")


def test_folder_pattern_rejects_non_canonical():
    """FOLDER_PATTERN respinge formate non-canonice."""
    p = audit_documente_sursa.FOLDER_PATTERN
    assert not p.match("identitate")  # lipsește prefix
    assert not p.match("1_identitate")  # un singur digit
    assert not p.match("ab_identitate")  # non-digit
    assert not p.match("01")  # lipsește categorie


def test_file_pattern_matches_canonical():
    """FILE_PATTERN acceptă YYYY-MM-DD_descriere.{pdf,jpeg,jpg,png} case-insensitive."""
    p = audit_documente_sursa.FILE_PATTERN
    assert p.match("2026-04-17_endoscopie_genesis.pdf")
    assert p.match("2024-05-30_dosar_upu_pag1.jpeg")
    assert p.match("2026-04-20_ct_torace.PDF")  # case-insensitive
    assert p.match("2026-04-17_buletin.jpg")
    assert p.match("2026-04-17_doc.png")


def test_file_pattern_rejects_non_canonical():
    """FILE_PATTERN respinge formate non-canonice."""
    p = audit_documente_sursa.FILE_PATTERN
    assert not p.match("endoscopie.pdf")  # lipsește data
    assert not p.match("2026-4-17_doc.pdf")  # data malformată (luna 1 cifră)
    assert not p.match("2026-04-17_doc.docx")  # extensie nepermisă
    assert not p.match("2026-04-17.pdf")  # lipsește descriere


def test_collect_intermediate_files_empty_folder(tmp_path):
    """Folder fără .meta.json → set gol."""
    folder = tmp_path / "01_test"
    folder.mkdir()
    result = audit_documente_sursa.collect_intermediate_files(folder)
    assert result == set()


def test_collect_intermediate_files_with_artifacts(tmp_path):
    """Meta.json cu intermediate_artifacts.files → set populat."""
    folder = tmp_path / "01_test"
    folder.mkdir()
    meta = folder / "doc.pdf.meta.json"
    meta.write_text(
        json.dumps({
            "tip_document": "test",
            "intermediate_artifacts": {"files": ["page1.jpeg", "page2.jpeg"]},
        }),
        encoding="utf-8",
    )
    result = audit_documente_sursa.collect_intermediate_files(folder)
    assert result == {"page1.jpeg", "page2.jpeg"}


def test_collect_intermediate_files_invalid_meta_json(tmp_path):
    """Meta.json corupt → set gol (nu crash)."""
    folder = tmp_path / "01_test"
    folder.mkdir()
    meta = folder / "doc.pdf.meta.json"
    meta.write_text("not json {{{", encoding="utf-8")
    result = audit_documente_sursa.collect_intermediate_files(folder)
    assert result == set()


def test_collect_intermediate_files_no_artifacts_field(tmp_path):
    """Meta.json fără câmpul intermediate_artifacts → set gol."""
    folder = tmp_path / "01_test"
    folder.mkdir()
    meta = folder / "doc.pdf.meta.json"
    meta.write_text(json.dumps({"tip_document": "test"}), encoding="utf-8")
    result = audit_documente_sursa.collect_intermediate_files(folder)
    assert result == set()


def test_audit_skips_missing_docs_dir(monkeypatch, tmp_path):
    """Dacă DOCS nu există → audit() returnează None graceful."""
    monkeypatch.setattr(audit_documente_sursa, "DOCS", tmp_path / "nonexistent")
    result = audit_documente_sursa.audit()
    assert result is None
