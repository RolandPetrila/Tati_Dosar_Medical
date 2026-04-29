#!/usr/bin/env python3
"""R31 — Build CORESPONDENTA_INDEX.md from Gmail thread files.

Sinteză toate threadurile Gmail din Dosar_Medical/corespondenta/*.md într-un
index unic + sumar per thread (frontmatter YAML + sinteză automată), optim
pentru retrieval Claude Projects.

Output: _projects_sync/CORESPONDENTA_INDEX.md
Trigger: orice modificare la Dosar_Medical/corespondenta/*.md (auto via pre-commit hook).
"""

import re
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
COR_DIR = ROOT / "Dosar_Medical" / "corespondenta"
OUTPUT = ROOT / "_projects_sync" / "CORESPONDENTA_INDEX.md"

# Excluse din bundle (sunt fișiere index/meta, nu threaduri reale)
EXCLUDE_NAMES = {"INDEX.md", "README.md"}


def parse_frontmatter(text):
    """Extract YAML frontmatter (între --- ... ---) ca dict simplu."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]
    fm = {}
    current_key = None
    for line in fm_text.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - "):
            # list item
            if current_key:
                fm.setdefault(current_key, [])
                if isinstance(fm[current_key], list):
                    fm[current_key].append(line[4:].strip())
        elif ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            current_key = k.strip()
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                fm[current_key] = [x.strip().strip('"') for x in v[1:-1].split(",") if x.strip()]
            elif v:
                fm[current_key] = v
            else:
                fm[current_key] = []
    return fm, body


def extract_synthesis(body):
    """Extract '## Sinteză automată' section if present, else first 30 lines."""
    m = re.search(r"^## Sinteză automată\n(.*?)(?=^## |^---)", body, re.DOTALL | re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Fallback: primele 30 linii non-goale
    lines = [l for l in body.splitlines() if l.strip()]
    return "\n".join(lines[:30])


def collect_threads():
    """Returnează lista threaduri Gmail, sortate cronologic descendent."""
    files = []
    for f in COR_DIR.glob("*.md"):
        if f.name in EXCLUDE_NAMES:
            continue
        files.append(f)
    files.sort(key=lambda p: p.name, reverse=True)
    return files


def render_thread(md_path):
    """Render un thread ca secțiune MD în index."""
    text = md_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    subject = fm.get("subject", md_path.stem)
    if isinstance(subject, list):
        subject = subject[0] if subject else md_path.stem
    thread_id = fm.get("thread_id", "—")
    data_start = fm.get("data_start", "—")
    data_ultim = fm.get("data_ultim", "—")
    status = fm.get("status", "—")
    mesaje = fm.get("mesaje_count", "—")
    participanti = fm.get("participanti", [])
    if isinstance(participanti, str):
        participanti = [participanti]
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]

    slug = md_path.stem.replace("_", "-")
    synthesis = extract_synthesis(body)

    lines = [
        f"\n---\n\n## <a name=\"{slug}\"></a> {subject}\n",
        f"\n**Fișier:** `Dosar_Medical/corespondenta/{md_path.name}`",
        f" · **Thread ID:** `{thread_id}`",
        f" · **Status:** {status}\n",
        f"\n**Cronologie:** {data_start} → {data_ultim} · **Mesaje:** {mesaje}\n",
    ]

    if participanti:
        lines.append("\n**Participanți:**\n")
        for p in participanti:
            lines.append(f"- {p}\n")

    if tags:
        tags_str = " · ".join(f"`{t}`" for t in tags)
        lines.append(f"\n**Tags:** {tags_str}\n")

    if synthesis:
        lines.append("\n### Sinteză\n\n")
        lines.append(synthesis)
        lines.append("\n")

    lines.append(
        f"\n> 📩 Pentru cronologia COMPLETĂ a mesajelor (text integral) "
        f"vezi sursa: `Dosar_Medical/corespondenta/{md_path.name}`\n"
    )

    return "".join(lines)


def build_index():
    threads = collect_threads()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        "# CORESPONDENȚĂ MEDICALĂ — Index threaduri Gmail\n",
        f"\n**Generat automat:** {now}",
        " · **Sursă:** `Dosar_Medical/corespondenta/*.md`",
        f" · **Total threaduri:** {len(threads)}\n",
        "\n> **Scop:** retrieval rapid pentru consult / discuție clinică — sinteze + frontmatter cheie. Pentru text INTEGRAL al mesajelor, deschide fișierul thread original în repo.",
        "\n>",
        "\n> **NU edita acest fișier direct** — regenerat la fiecare commit cu modificare în `Dosar_Medical/corespondenta/*.md` (R31 + pre-commit hook).\n",
        "\n---\n\n## 📚 Cuprins\n",
    ]

    for f in threads:
        try:
            text = f.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(text)
            subject = fm.get("subject", f.stem)
            if isinstance(subject, list):
                subject = subject[0] if subject else f.stem
            data_ultim = fm.get("data_ultim", "—")
            status = fm.get("status", "")
            slug = f.stem.replace("_", "-")
            lines.append(f"\n- [{data_ultim} · {subject}](#{slug}) — {status}")
        except Exception:
            lines.append(f"\n- ⚠️ {f.name} (parse error)")

    for f in threads:
        try:
            section = render_thread(f)
            lines.append(section)
        except Exception as e:
            lines.append(f"\n## ❌ {f.name}\n\n```\n{e}\n```\n")

    lines.append("\n---\n")
    lines.append(f"\n_Sfârșit index. {len(threads)} threaduri sintetizate._\n")

    return "".join(lines)


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    index = build_index()
    OUTPUT.write_text(index, encoding="utf-8")
    size_kb = OUTPUT.stat().st_size / 1024
    threads_count = len(collect_threads())
    print(f"  ✅ Generat: CORESPONDENTA_INDEX.md ({size_kb:.1f} KB, {threads_count} threaduri)")


if __name__ == "__main__":
    main()
