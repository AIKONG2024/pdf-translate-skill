#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill="$root/pdf-translate/SKILL.md"

test -f "$skill"
grep -q '^---$' "$skill"
grep -q '^name: pdf-translate$' "$skill"
grep -q '^description: ' "$skill"
test -f "$root/pdf-translate/scripts/pdf_translate.py"
test -f "$root/pdf-translate/scripts/validate_outputs.py"
test -f "$root/pdf-translate/references/engines.md"
test -f "$root/pdf-translate/references/services.md"
test -f "$root/docs/install.md"
test -f "$root/docs/setup.md"
test -f "$root/docs/security-and-secrets.md"
test -f "$root/docs/features/pdf-translate.md"
python -m py_compile "$root/pdf-translate/scripts/pdf_translate.py" "$root/pdf-translate/scripts/validate_outputs.py"
echo "skill validation ok"
