# pdf-translate-skill

[ENGLISH](README.md)

PDF 레이아웃을 가능한 한 유지하면서 에이전트가 PDF를 번역하도록 돕는 스킬입니다.

- Codex, Claude Code, agents 호환 런타임에서 사용 가능
- 기본 엔진은 PDFMathTranslate의 공식 `pdf2zh` CLI
- 최종 산출물은 번역된 PDF

-그림위치-

## 설치

### HUMAN

에이전트에게 이렇게 요청하세요:

```text
AIKONG2024/pdf-translate-skill 스킬 설정해줘
```

### AGENT

<details>
<summary>설치 지침 열기</summary>

이 저장소를 읽고 현재 에이전트 런타임이 사용하는 skill 디렉터리에 `pdf-translate` 스킬을 설치하세요.

설치 대상 폴더:

```text
pdf-translate/
```

설치된 스킬에는 다음 항목이 포함되어야 합니다:

```text
pdf-translate/SKILL.md
pdf-translate/scripts/
pdf-translate/references/
pdf-translate/agents/
```

현재 런타임이 지원하는 설치 방식을 사용하세요:

- GitHub skill 설치를 지원하면 `AIKONG2024/pdf-translate-skill` 저장소의 `pdf-translate` 경로를 설치하세요.
- `skills` CLI를 지원하면 다음 명령을 사용하세요:

```bash
npx --yes skills add https://github.com/AIKONG2024/pdf-translate-skill --all -g
```

- 수동 local skill만 지원하면 `pdf-translate/` 폴더를 해당 런타임의 skill 디렉터리에 복사하세요.

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

유료 또는 API 키가 필요한 번역 서비스를 사용할 경우, 해당 서비스에 필요한 환경 변수만 설정하면 됩니다.

주요 예시:

| Provider | Environment variables |
| --- | --- |
| Google | 없음 |
| DeepL | `DEEPL_AUTH_KEY` |
| OpenAI | `OPENAI_API_KEY`, 선택적으로 `OPENAI_MODEL` |
| Gemini | `GEMINI_API_KEY`, 선택적으로 `GEMINI_MODEL` |
| Ollama | `OLLAMA_HOST`, `OLLAMA_MODEL` |

## 사용

에이전트에게 이렇게 요청하세요:

```text
이 PDF를 프랑스어로 번역하고 레이아웃을 유지해줘: /path/to/paper.pdf
```

에이전트는 원문 언어와 목표 언어를 확인해야 합니다. 클라우드 번역 서비스를 사용할 경우, PDF에서 추출한 텍스트를 해당 제공자에게 전송해도 되는지 먼저 확인해야 합니다.

## 출력

```text
outputs/pdf_translate/<run-id>/
├── source/
│   └── original.pdf
├── translated-<target-lang>.pdf
└── translation-summary.md
```

사용할 최종 파일은 다음입니다:

```text
translated-<target-lang>.pdf
```

## 참고

- 이 스킬은 PDFMathTranslate, BabelDOC, 모델, wheel, 샘플 PDF를 저장소에 포함하지 않습니다.
- 현재 공식 `pdf2zh` 릴리스는 BabelDOC 같은 upstream 런타임 의존성을 설치할 수 있습니다.
- 이 스킬은 기본적으로 선택 기능인 `--babeldoc` 백엔드를 호출하지 않습니다.
- 스캔본 또는 이미지 기반 PDF는 먼저 OCR을 수행해야 하며, 그렇지 않으면 결과가 제한될 수 있습니다.
- 자세한 사용법은 [docs/features/pdf-translate.md](docs/features/pdf-translate.md)에 있습니다.
