# Engines

## Default Engine

`pdf2zh` is the default engine.

It is the official CLI/package from PDFMathTranslate and performs the layout-preserving PDF translation work. This skill orchestrates the run, provider selection, output normalization, and validation.

## Dependency Boundary

The skill does not vendor PDFMathTranslate, BabelDOC, model files, wheels, or sample PDFs.

Current official `pdf2zh` releases may install runtime dependencies such as BabelDOC. This skill does not invoke the optional `--babeldoc` backend by default.

## Supported Script Engines

| Engine | Purpose | Public status |
| --- | --- | --- |
| `pdf2zh` | Real PDF translation through official PDFMathTranslate CLI | Default |
| `mock` | Test-only engine that copies the source PDF into the expected output shape | Internal test only |

Do not document `mock` as a real translation option for end users.

## Output Contract

The helper script creates one run directory:

```text
outputs/pdf_translate/<run-id>/
```

The final PDF is:

```text
translated-<target-lang>.pdf
```

The script removes default bilingual output and temporary render PNGs unless debug behavior is explicitly added later.

