#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / ".claude" / "agents" / "analista-documental-requisitos.md"

REQUIRED_KNOWLEDGE = [
    "README.md",
    "decision-rules.md",
    "evidence-scope.md",
    "workflow.md",
    "elicitation.md",
    "interviews.md",
    "workshops-observation.md",
    "elicitation-to-requirements.md",
    "requirement-quality.md",
    "quality-checklist.md",
    "acceptance-criteria.md",
    "prioritization.md",
    "baseline-change-control.md",
    "bpmn-modeling.md",
    "uat.md",
    "standards-hierarchy.md",
    "ai-metrics.md",
    "handoffs.md",
    "open-questions.md",
]

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)

if not AGENT.exists():
    fail(f"No existe {AGENT.relative_to(ROOT)}")

text = AGENT.read_text(encoding="utf-8")

if not text.startswith("---\n"):
    fail("El archivo del agente no empieza con frontmatter YAML.")

parts = text.split("---", 2)
if len(parts) < 3:
    fail("Frontmatter incompleto.")

frontmatter = parts[1]

for field in ("name", "description"):
    if not re.search(rf"(?m)^\s*{re.escape(field)}\s*:", frontmatter):
        fail(f"Falta campo obligatorio: {field}")

name_match = re.search(r"(?m)^\s*name\s*:\s*([^\n]+)", frontmatter)
name = name_match.group(1).strip().strip("'\"") if name_match else ""
if not name or name.startswith("-") or ":" in name:
    fail(f"Nombre de agente inválido: {name!r}")

if "tools: Read, Glob, Grep" not in frontmatter:
    fail("El agente v0.1 debe permanecer read-only con Read, Glob y Grep.")

knowledge_dir = ROOT / "agents" / "analista-documental-requisitos"
missing = [name for name in REQUIRED_KNOWLEDGE if not (knowledge_dir / name).exists()]
if missing:
    fail("Faltan módulos de conocimiento: " + ", ".join(missing))

constitution = ROOT / "constitution" / "engineering-constitution.md"
if not constitution.exists():
    fail("Falta la constitución de ingeniería.")

print("OK: configuración estática del agente válida.")
print(f"Agente: {name}")
print(f"Módulos de conocimiento: {len(REQUIRED_KNOWLEDGE)}")
