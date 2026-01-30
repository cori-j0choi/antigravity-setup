[English](README.md)

# Antigravity Setup Guide

**Antigravity**는 LLM 에이전트(Planner, Architect, Developer, Tester, Reviewer)가 유기적으로 협업하며 지속적으로 학습하는 **자율형 개발 환경** 설정입니다.

이 문서는 `antigravity-setup` 패키지의 설치, 설정 및 사용 방법을 안내합니다.

## 1. 개요 (Overview)

이 설정 패키지는 다음 핵심 가치를 제공합니다:
- **Role-Based Collaboration**: 명확한 역할 분담과 책임 정의 (`agents/roles.yaml`).
- **Manus Protocol Implementation**: 체계적인 협업 프로토콜 (`agents/workflow.md`).
- **Language flexibility**: 기본은 영어지만, 설정에 따라 한글 사용 가능 (`rules/00_language.rules.md`).
- **Meta-Learning**: 실패로부터 배우고 진화하는 파이프라인 (`memory/failures/`, `skills/continuous-learning`).

## 2. 설치 및 설정 (Installation & Setup)

### 2.1 사전 요구사항 (Prerequisites)
- **Node.js** (v18 이상): MCP 서버 실행을 위해 필요합니다.
- **Python** (v3.10 이상): Python 관련 스킬 활용 시 권장됩니다.
- **Git**: 버전 관리를 위해 필수입니다.

### 2.2 MCP 서버 설치
`mcp/mcp_config.json`에 정의된 도구들을 활성화하기 위해 필요한 패키지를 설치합니다.

```bash
# 의존성 패키지(MCP 서버) 일괄 설치
npm install

# 또는 NPX로 설치 (권장)
npx antigravity-setup
```

### 2.3 환경 변수 설정
`mcp_config.json` 또는 시스템 환경 변수에 다음 값을 설정해야 합니다.

- `GITHUB_PERSONAL_ACCESS_TOKEN`: GitHub 저장소 접근 권한이 있는 토큰.

### 2.4 에이전트 설정 연동
사용 중인 LLM 에이전트 시스템(예: Claude Desktop, Custom Agent Runner)에 이 디렉토리를 **Context**로 제공하거나 **Config Path**로 지정해야 합니다.

- **Context Path**: `d:\2026\08_antigravity_everything_code\antigravity-setup`

### 2.5 컨텍스트 인식 설정 (Context-Aware Setup)
설치 과정(`npx` 또는 수동)에서 타겟 프로젝트를 분석할지 묻습니다.
- **동작**: 프로젝트 언어(Python, Java 등)와 프레임워크를 자동 탐지합니다.
- **결과**: `rules/tech_stack.md` 파일을 생성합니다.
- **효과**: 모든 에이전트가 별도의 설정 없이도 감지된 기술 스택에 맞춰 코드를 작성합니다.

### 2.6 자동 구성 (컨텍스트 파일)
마지막으로, `bin/configure.js`가 실행되어 프로젝트 루트에 `AGENTS.md` 파일을 생성합니다.
- **목적**: LLM / 에이전트를 위한 단일 진입점(Context File)을 제공합니다.
- **내용**: `roles.yaml`, `workflow.md`, 그리고 생성된 `tech_stack.md`를 참조합니다.
- **사용법**: 이 파일을 IDE에 열어두거나 에이전트의 Context로 전달하기만 하면 됩니다.

## 3. 사용 가이드 (Usage Guide)

### 3.1 프로젝트 시작 (`/plan`)
새로운 기능을 개발하거나 프로젝트를 시작할 때 Planner를 호출합니다.

```
/plan [프로젝트명] [요구사항 설명]
```

- Planner는 `memory/lessons/`를 검토하여 과거의 교훈을 반영한 `task_plan.md`를 작성합니다.
- **[NEW]** `/spec` 명령어를 통해 상세 명세서를 작성할 수도 있습니다.
- 사용자의 **승인(Confirmation)**이 있어야만 다음 단계로 넘어갑니다.

### 3.2 구현 및 테스트 (`/tdd`)
설계가 완료되면 Developer와 Tester가 구현을 시작합니다.

```
/tdd [기능명]
```

- **Red**: 실패하는 테스트 작성.
- **Green**: 기능 구현.
- **Refactor**: 코드 개선.
- 만약 구현 중 에러가 발생하면 `memory/failures/`에 자동으로 기록됩니다.

### 3.3 검증 및 리포트 (`/verify`)
구현이 완료되면 품질을 검증합니다.

```
/verify
```

- 빌드, 테스트, 린트, 보안 검사를 수행하고 `reports/verification/`에 리포트를 생성합니다.

### 3.4 회고 및 학습 (`/learn`)
작업이 완료되면 교훈을 추출하여 저장합니다.

```
/learn
```

- 실패 로그를 분석하여 `memory/lessons/`에 영구적인 지식(Instinct)으로 저장합니다.

## 4. 디렉토리 구조 (Directory Structure)

```
antigravity-setup/
├── agents/                  # 에이전트 역할(roles.yaml) 및 워크플로우(workflow.md)
├── skills/                  # 단계별 전문 스킬 (기획, 설계, 구현, 테스트, 학습)
│   ├── specification-writer # [NEW] 명세서 작성 스킬
│   └── verification-reporter # [NEW] 검증 리포트 스킬
├── rules/                   # [제1원칙] 한글 사용 및 코딩 표준
├── mcp/                     # MCP 도구 설정 (mcp_config.json)
├── tools/                   # 슬래시 커맨드 정의 (commands.md)
├── memory/                  # 메타 러닝 저장소 (failures/, lessons/)
├── reports/                 # [NEW] 산출물 저장소 (specs/, verification/)
├── hooks/                   # [NEW] 자동화 훅 설정 (hooks.json)
└── scripts/
    └── swarm/               # [NEW] 병렬 에이전트 오케스트레이션 (orchestrator.py)
```

## 5. Hooks System (자동화 훅)
`hooks/hooks.json`에 정의된 자동화 훅이 워크플로우를 보조합니다:
- **Session Start**: `memory/lessons/`에서 이전 교훈을 로드하여 컨텍스트를 제공합니다.
- **Session End**: 세션 로그를 `memory/sessions/`에 저장합니다.
- **Pre-Tool Safety**:
    - `git push` 전 검증 리마인더를 표시합니다.
    - 규칙에 어긋나는 무분별한 마크다운 파일 생성을 방지합니다.
- **Quality Checks**: 파일 수정 후 남아있는 `console.log`를 감지하여 경고합니다.

## 6. 실행 모드 (Execution Modes)
Antigravity는 작업 복잡도에 따라 두 가지 모드로 실행할 수 있습니다.

### 6.1 대화형 모드 (Interactive Mode)
**추천**: 일상적인 개발, TDD, 단일 기능 구현.
- **방법**: IDE(Cursor, Windsurf) 채팅창에서 LLM과 대화합니다.
- **실행**: `/plan`, `/tdd` 등의 명령어를 입력합니다.
- **원리**: LLM이 `AGENTS.md` 컨텍스트를 기반으로 에이전트(Planner, Developer) 역할을 수행하며 도구를 실행합니다.

### 6.2 자율 모드 (Autonomous Swarm)
**추천**: 복잡한 마이그레이션, 대규모 리팩토링, 다중 파일 작업.
- **방법**: Python 오케스트레이터 스크립트를 실행합니다.
- **실행**: `python scripts/swarm/orchestrator.py`
- **원리**: 여러 에이전트 인스턴스가 병렬로 실행되며 체크리스트를 기반으로 협업합니다.

## 7. 고급 기능 (Advanced Features)

### 7.1 Parallel Swarm (병렬 실행)
복잡한 작업을 병렬로 처리합니다.
```bash
python scripts/swarm/orchestrator.py
```

### 6.2 Auto-Swarm Skill
작업이 복잡하면(파일 3개 이상) 에이전트가 자동으로 팀을 구성합니다.
- **Trigger**: `skills/common/antigravity-swarm/SKILL.md`

### 6.3 Vibe Coding (바이브 코딩)
"Think-Run-Feedback" 루프를 강제하여 빠른 개발 속도를 유지합니다.
- **Skill**: `skills/common/vibe-coding/SKILL.md`
- **Agent**: `Vibe_Coding_Coach`
- **Support**: `Synthetic Data` 스킬로 테스트 데이터 자동 생성.

### 6.4 MSA Architecture
에이전트와 도구를 마이크로 서비스처럼 분리하여 관리합니다.
- **Rule**: `rules/msa_architecture.rules.md`
- **Agent**: `MCP_Steward`

## 7. 기여 (Contributing)
새로운 스킬을 추가하거나 규칙을 변경하려면 해당 디렉토리의 파일을 수정하고, `agents/workflow.md`에 반영해 주세요.
