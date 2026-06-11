# do-you-want-translate-pdf-file-skill

[ENGLISH](README.md)

PDF 레이아웃을 가능한 한 유지하면서 에이전트가 PDF를 번역하도록 돕는 스킬입니다.

- Codex, Claude Code, agents 호환 런타임에서 사용 가능
- 기본 엔진은 PDFMathTranslate의 공식 `pdf2zh` CLI
- 최종 산출물은 번역된 PDF

<img width="450" height="600" alt="image" src="https://github.com/user-attachments/assets/c1cd0770-ae2a-4df3-8f76-679c9da0858b" /><img width="450" height="600" alt="image" src="https://github.com/user-attachments/assets/2f6f2b6e-4e0a-4096-ba81-1334f13d678a" />

## 설치

### HUMAN

에이전트에게 이렇게 요청하세요:

```text
AIKONG2024/do-you-want-translate-pdf-file-skill 스킬 설정해줘
```

### AGENT

<details>
<summary>설치 지침 열기</summary>

이 저장소를 읽고 현재 에이전트 런타임이 사용하는 skill 디렉터리에 `do-you-want-translate-pdf-file-skill` 스킬을 설치하세요.

설치 대상 폴더:

```text
do-you-want-translate-pdf-file-skill/
```

설치된 스킬에는 다음 항목이 포함되어야 합니다:

```text
do-you-want-translate-pdf-file-skill/SKILL.md
do-you-want-translate-pdf-file-skill/scripts/
do-you-want-translate-pdf-file-skill/references/
do-you-want-translate-pdf-file-skill/agents/
```

현재 런타임이 지원하는 설치 방식을 사용하세요:

- GitHub skill 설치를 지원하면 `AIKONG2024/do-you-want-translate-pdf-file-skill` 저장소의 `do-you-want-translate-pdf-file-skill` 경로를 설치하세요.
- `skills` CLI를 지원하면 다음 명령을 사용하세요:

```bash
npx --yes skills add https://github.com/AIKONG2024/do-you-want-translate-pdf-file-skill --all -g
```

- 수동 local skill만 지원하면 `do-you-want-translate-pdf-file-skill/` 폴더를 해당 런타임의 skill 디렉터리에 복사하세요.

설치 후 런타임 의존성을 확인하세요:

```bash
pdf2zh --help
```

`pdf2zh`가 없다면 PDFMathTranslate의 공식 CLI를 설치하세요:

```bash
python -m pip install pdf2zh
```

새 skill 인식을 위해 런타임 재시작 또는 reload가 필요하면 사용자에게 안내하세요.

</details>

## 설정

기본 번역 서비스는 Google이므로 기본 실행에는 API 키가 필요하지 않습니다. 다만 클라우드 번역 서비스는 PDF에서 추출한 텍스트를 외부 제공자에게 보낼 수 있으므로, 실행 전에 에이전트가 사용자에게 확인해야 합니다.

더 높은 번역 품질이나 로컬/비공개 번역을 원하면 provider를 선택하고, 해당 provider에 필요한 환경 변수만 설정하면 됩니다.

| Provider | Service | Environment variables |
| --- | --- | --- |
| Google | `google` | 없음 |
| Bing | `bing` | 없음 |
| DeepL | `deepl` | `DEEPL_AUTH_KEY` |
| DeepLX | `deeplx` | `DEEPLX_ENDPOINT` |
| Ollama | `ollama` | `OLLAMA_HOST`, `OLLAMA_MODEL` |
| OpenAI | `openai` | `OPENAI_API_KEY`, 선택적으로 `OPENAI_BASE_URL`, `OPENAI_MODEL`, `OPENAI_STOP_TOKENS`, `OPENAI_MAX_TOKENS` |
| Azure OpenAI | `azure-openai` | `AZURE_OPENAI_BASE_URL`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_MODEL` |
| Gemini | `gemini` | `GEMINI_API_KEY`, 선택적으로 `GEMINI_MODEL` |
| Azure Translator | `azure` | `AZURE_ENDPOINT`, `AZURE_API_KEY` |
| Tencent | `tencent` | `TENCENTCLOUD_SECRET_ID`, `TENCENTCLOUD_SECRET_KEY` |
| Dify | `dify` | `DIFY_API_URL`, `DIFY_API_KEY` |
| AnythingLLM | `anythingllm` | `AnythingLLM_URL`, `AnythingLLM_APIKEY` |
| Argos Translate | `argos` | Argos language packages |
| Grok | `grok` | `GORK_API_KEY`, `GORK_MODEL` |
| DeepSeek | `deepseek` | `DEEPSEEK_API_KEY`, `DEEPSEEK_MODEL` |
| MiniMax | `minimax` | `MINIMAX_API_KEY`, `MINIMAX_MODEL` |
| OpenAI-compatible | `openailiked` | `OPENAILIKED_BASE_URL`, `OPENAILIKED_API_KEY`, `OPENAILIKED_MODEL`, 선택적으로 `OPENAILIKED_STOP_TOKENS`, `OPENAILIKED_MAX_TOKENS` |

예시:

```powershell
# Windows PowerShell
$env:OPENAI_API_KEY="your-api-key"
$env:OPENAI_MODEL="gpt-4o-mini"
```

```bash
# macOS / Linux
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4o-mini"
```

Ollama 로컬 번역을 사용할 경우:

```bash
export OLLAMA_HOST="http://127.0.0.1:11434"
export OLLAMA_MODEL="gemma2"
```

## 사용

에이전트에게 이렇게 요청하세요:

```text
이 PDF를 한국어로 번역하고 레이아웃을 유지해줘.
```

요청할 때 PDF를 첨부하세요. 에이전트는 원문 언어와 목표 언어를 확인해야 합니다. 클라우드 번역 서비스를 사용할 경우, PDF에서 추출한 텍스트를 해당 제공자에게 전송해도 되는지 먼저 확인해야 합니다.

## 출력

```text
outputs/pdf_translate/<run-id>/
├── source/
│   └── original.pdf
├── translated-<target-lang>.pdf
└── translation-summary.md
```

최종 생성 파일:

```text
translated-<target-lang>.pdf
```

## 출처 및 라이선스

이 스킬은 [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)의 공식 `pdf2zh` CLI를 사용해 PDF 레이아웃 보존 번역을 수행합니다.

PDFMathTranslate / `pdf2zh`는 `AGPL-3.0` 라이선스로 배포됩니다. 이 저장소는 해당 라이브러리나 모델 파일을 포함하지 않으며, 외부 `pdf2zh` CLI를 실행하도록 안내하는 MIT 라이선스 skill입니다.
