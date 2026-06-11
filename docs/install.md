# Install

## Recommended Flow

1. Install the skill bundle.
2. Run setup checks.
3. Ask the agent to translate a PDF.

## Ask Your Agent

Paste this into Codex or Claude Code:

```text
Read this repository's install guide and install the pdf-translate skill globally. After installation, verify the skill files and tell me the next command to translate a PDF.
```

## Direct Install

Use one installer command:

```bash
npx --yes skills add https://github.com/<owner>/pdf-translate-skill --all -g
```

Equivalent runners:

```bash
pnpm dlx skills add https://github.com/<owner>/pdf-translate-skill --all -g
bunx skills add https://github.com/<owner>/pdf-translate-skill --all -g
```

## Local Repository Test

From the repository root:

```bash
npx --yes skills add . --all -g
npx --yes skills ls -g
```

## Runtime Packages

For real translation runs, install the official `pdf2zh` CLI from PDFMathTranslate:

```bash
python -m pip install pdf2zh
pdf2zh --help
```

If global install is blocked by policy, explain the blocker and set `PDF2ZH_BIN` to an approved local executable path.

## Verify This Repository

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest tests -q
bash scripts/validate-skills.sh
```
