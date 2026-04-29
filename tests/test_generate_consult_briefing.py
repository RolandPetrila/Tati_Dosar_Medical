"""Smoke test pentru scripts/generate_consult_briefing.py (Faza 3 plan implementare).

Validează:
  - happy path: build_docx() pentru cele 3 tipuri (oncolog/cardiolog/endocrin)
  - edge case: tip consult invalid → False + mesaj eroare
  - main() E2E cu sys.argv mock + RAPOARTE redirected → DOCX + .meta.json
  - pure functions: extract_section()
  - non-destructive: tot output în tmp_path, NU suprascrie 2026-05-04 Anater
"""

import json
import sys

import generate_consult_briefing as briefing


def test_consult_templates_have_required_keys():
    """Toate cele 3 template-uri au structura cerută."""
    for tip in ("oncolog", "cardiolog", "endocrin"):
        assert tip in briefing.CONSULT_TEMPLATES
        t = briefing.CONSULT_TEMPLATES[tip]
        assert "titlu" in t
        assert "intrebari" in t
        assert isinstance(t["intrebari"], list)
        assert len(t["intrebari"]) >= 3


def test_build_docx_oncolog(tmp_path):
    """Happy path: build_docx pentru oncolog → DOCX valid."""
    output = tmp_path / "test_briefing.docx"
    success = briefing.build_docx(
        consult_type="oncolog",
        data="2026-05-04",
        medic="Dr. Test Anater",
        unitate="OncoHelp Test",
        output_path=output,
    )
    assert success is True
    assert output.exists()
    assert output.stat().st_size > 5_000  # DOCX minim ~5KB


def test_build_docx_cardiolog(tmp_path):
    """Happy path: build_docx pentru cardiolog."""
    output = tmp_path / "test_briefing.docx"
    success = briefing.build_docx(
        consult_type="cardiolog",
        data="2026-05-15",
        medic="Dr. Test Cardiolog",
        unitate="Cardio Center",
        output_path=output,
    )
    assert success is True
    assert output.exists()


def test_build_docx_endocrin(tmp_path):
    """Happy path: build_docx pentru endocrin."""
    output = tmp_path / "test_briefing.docx"
    success = briefing.build_docx(
        consult_type="endocrin",
        data="2026-06-01",
        medic="Dr. Test Endocrin",
        unitate="Endo Clinic",
        output_path=output,
    )
    assert success is True
    assert output.exists()


def test_build_docx_invalid_consult_type(tmp_path, capsys):
    """Edge case: tip consult necunoscut → False + mesaj eroare."""
    output = tmp_path / "test_briefing.docx"
    success = briefing.build_docx(
        consult_type="oftalmolog",  # invalid
        data="2026-05-04",
        medic="Dr. Test",
        unitate="Test Unit",
        output_path=output,
    )
    assert success is False
    captured = capsys.readouterr()
    assert "tip consult necunoscut" in captured.out
    assert not output.exists()


def test_extract_section_basic():
    """extract_section pe structură cu 2 secțiuni → returnează doar secțiunea cerută."""
    md = """## Section A

Content A line 1
Content A line 2

## Section B

Content B
"""
    result = briefing.extract_section(md, r"^## Section A$")
    assert "Section A" in result
    assert "Content A line 1" in result
    assert "Content A line 2" in result
    assert "Content B" not in result
    assert "Section B" not in result


def test_extract_section_not_found():
    """extract_section când header-ul lipsește → string gol."""
    md = "## Other\n\nNothing here\n"
    result = briefing.extract_section(md, r"^## NonExistent$")
    assert result == ""


def test_extract_section_stops_at_next_header():
    """extract_section se oprește la următorul `## ` sau `### `."""
    md = """## A

content A

### A.1

sub A.1

## B

content B"""
    result = briefing.extract_section(md, r"^## A$")
    assert "content A" in result
    assert "sub A.1" not in result
    assert "content B" not in result


def test_main_creates_docx_and_meta_e2e(tmp_path, monkeypatch):
    """E2E: main() cu argv mock + RAPOARTE tmp → DOCX + .meta.json corecte."""
    monkeypatch.setattr(briefing, "RAPOARTE", tmp_path)
    monkeypatch.setattr(sys, "argv", [
        "generate_consult_briefing.py",
        "--consult", "oncolog",
        "--data", "2026-05-04",
        "--medic", "Dr. Test Anater",
        "--unitate", "OncoHelp Test",
    ])

    rc = briefing.main()

    assert rc == 0
    docx_path = tmp_path / "2026-05-04_briefing_consult_oncolog.docx"
    meta_path = tmp_path / "2026-05-04_briefing_consult_oncolog.docx.meta.json"
    assert docx_path.exists()
    assert meta_path.exists()


def test_main_meta_json_structure(tmp_path, monkeypatch):
    """Meta.json companion conține toate câmpurile cerute."""
    monkeypatch.setattr(briefing, "RAPOARTE", tmp_path)
    monkeypatch.setattr(sys, "argv", [
        "generate_consult_briefing.py",
        "--consult", "cardiolog",
        "--data", "2026-05-20",
        "--medic", "Dr. X",
        "--unitate", "Clinica Y",
    ])

    briefing.main()

    meta_path = tmp_path / "2026-05-20_briefing_consult_cardiolog.docx.meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    assert meta["tip_document"] == "briefing_consult_DOCX"
    assert meta["consult_type"] == "cardiolog"
    assert meta["data_consult"] == "2026-05-20"
    assert meta["medic"] == "Dr. X"
    assert meta["unitate"] == "Clinica Y"
    assert "generated_at" in meta
    assert "structura" in meta
    assert isinstance(meta["structura"], list)
    assert len(meta["structura"]) >= 6  # cele 7 secțiuni declarate


def test_main_invalid_consult_type_via_argparse(tmp_path, monkeypatch):
    """argparse refuză tip consult în afara choices → SystemExit."""
    import pytest
    monkeypatch.setattr(briefing, "RAPOARTE", tmp_path)
    monkeypatch.setattr(sys, "argv", [
        "generate_consult_briefing.py",
        "--consult", "oftalmolog",  # invalid
        "--data", "2026-05-04",
        "--medic", "Dr. Test",
        "--unitate", "Test",
    ])
    with pytest.raises(SystemExit):
        briefing.main()


def test_main_missing_required_arg_via_argparse(monkeypatch):
    """argparse refuză apel fără --consult → SystemExit."""
    import pytest
    monkeypatch.setattr(sys, "argv", [
        "generate_consult_briefing.py",
        "--data", "2026-05-04",
        "--medic", "Dr. Test",
        "--unitate", "Test",
    ])
    with pytest.raises(SystemExit):
        briefing.main()
