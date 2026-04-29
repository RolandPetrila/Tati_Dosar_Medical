"""Configurație pytest pentru smoke tests pe scripts/.

Adaugă scripts/ la sys.path așa că `import system_health_check` funcționează.
Testele folosesc monkeypatch pentru OUTPUT/RAPOARTE → izolare non-destructivă a
fișierelor de producție (SYSTEM_HEALTH.json, INDEX.json, AUDIT_DOCUMENTE_SURSA.md,
rapoarte_generate/*.docx). Datele de input rămân reale → smoke validează că
scripturile pot procesa proiectul real fără crash.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
