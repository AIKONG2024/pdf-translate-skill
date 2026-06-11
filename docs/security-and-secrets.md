# Security And Secrets

This skill declares required environment variable names and lets the user or agent runtime decide how to supply values.

## Cloud Transfer

Cloud providers may receive extracted PDF text. Before using a cloud service, the agent must ask:

```text
This translation service may send extracted PDF text to an external provider (<provider>). Do you want to continue?
```

## Secret Policy

- Do not commit real secrets.
- Do not place secret files in this repository.
- Prefer environment variables or the agent runtime's secret vault.
- If a key is missing, tell the user the exact variable name.
- Do not silently switch to another provider to avoid a missing key.

## Local Services

`ollama` and `argos` can be local options when installed and configured. They still require setup checks, but they do not require cloud-transfer confirmation.

## Sensitive PDFs

For private, confidential, medical, legal, financial, or unpublished documents, prefer local services or stop until the user explicitly approves cloud translation.
