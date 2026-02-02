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
- **Trend Alignment**: 트렌드 기반 스킬/에이전트 확장 (`reports/recommendations/`).

## 2. 설치 및 설정 (Installation & Setup)

### 2.1 사전 요구사항 (Prerequisites)
- **Node.js** (v18 이상): MCP 서버 실행을 위해 필요합니다.
- **Python** (v3.10 이상): Python 관련 스킬 활용 시 권장됩니다.
- **Git**: 버전 관리를 위해 필수입니다.

### 2.2 NPX를 통한 설치 (권장)
가장 쉬운 시작 방법입니다. 저장소를 복제하고 환경을 설정합니다.

```bash
# 기본적으로 ~/.agent/antigravity-setup 에 설치
npx antigravity-setup

# 또는 사용자 지정 디렉토리에 설치
npx antigravity-setup ./my-antigravity
```

### 2.3 수동 설치 (Manual Installation)
수동으로 복제하고 싶다면 다음을 수행하세요:

```bash
git clone https://github.com/cori-j0choi/antigravity-setup.git
cd antigravity-setup
npm install
```

### 2.4 환경 변수 설정 (Environment Variables Configuration)
`mcp_config.json` 또는 시스템 환경 변수에 다음 값을 설정해야 합니다.

- `GITHUB_PERSONAL_ACCESS_TOKEN`: GitHub 저장소 접근 권한이 있는 토큰.

### 2.6 대화형 설정 (Interactive Configuration)
설치 스크립트 `bin/configure.js`가 대화형으로 설정을 안내합니다:

1.  **Git 공급자 선택**: GitHub(기본값) 또는 Gitea 중 선택합니다.
2.  **인증 정보**:
    -   **GitHub**: Personal Access Token을 준비하세요.
    -   **Gitea**: 인스턴스 URL(예: `https://gitea.com`)과 Access Token을 입력합니다.
    -   **Gitea 모드**: Docker(추천) 또는 로컬 바이너리 실행 중 선택합니다.
3.  **컨텍스트 생성**: 프로젝트 루트에 `AGENTS.md`를 생성합니다.

> [!NOTE]
> **Git 설정 자동화**: 선택한 공급자에 맞춰 MCP 설정(`mcp_config.json`)이 자동으로 구성됩니다.

### 2.7 자동 구성 (Context File)
마지막으로, `bin/configure.js`가 실행되어 프로젝트 루트에 `AGENTS.md` 파일을 생성합니다.
- **목적**: LLM / 에이전트를 위한 단일 진입점(Context File)을 제공합니다.
- **내용**: `roles.yaml`, `workflow.md`, 그리고 생성된 `tech_stack.md`를 참조합니다.
- **사용법**: 이 파일을 IDE에 열어두거나 에이전트의 Context로 전달하기만 하면 됩니다.

> [!NOTE]
> **Git 인식 (Git-Awareness)**: 설정 과정에서 `.git` 폴더를 자동으로 감지합니다.
> - 발견 시: `github` MCP (Issue/PR)를 활성화합니다.
> - 미발견 시: 에러 방지를 위해 `github` 기능을 비활성화합니다.

## 3. 사용 가이드 (Usage Guide)

### 3.1 프로젝트 시작 (`/plan`)
1.  IDE(Cursor/Windsurf)를 열고 `AGENTS.md`를 활성화합니다(또는 내용을 채팅에 복사).
2.  **명령**: "시작하자. `/plan` 로그인 기능을 만들어줘."
3.  **Planner 에이전트**:
    -   요구사항을 분석하고 `tech_stack.md`와 Git 상태를 확인합니다.
    -   `task_plan.md`를 작성하고 질문합니다.
    -   **질문**: "이 계획을 Swarm으로 실행하시겠습니까?"
4.  **실행 (Execution)**:
    -   **Interactive**: 대화를 계속하며 직접 `/tdd` 진행.
    -   **Autonomous**: "응"이라고 답하면 `scripts/swarm/orchestrator.py`를 실행하여 자동 구현 시작.

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
- **[NEW]** `/eval`, `/redteam`, `/observe` 단계가 품질/보안/관측성을 강화합니다.

### 3.5 트렌드 레이더 (`/trend`)
최신 도구/에이전트/스킬을 검토하여 메타 파이프라인 품질을 개선합니다.

- 결과는 `reports/recommendations/`에 저장됩니다.

## 4. 디렉토리 구조 (Directory Structure)

```
antigravity-setup/
├── agents/                  # 에이전트 역할(roles.yaml) 및 워크플로우(workflow.md)
├── skills/                  # 단계별 전문 스킬
│   ├── 01_planning/         # 기획 스킬 (Trend Radar 등)
│   ├── 03_implementation/   # 구현 스킬 (Tool Reliability 등)
│   ├── 04_testing/          # 테스트 스킬 (Evals, Red-Team)
│   └── 05_learning/         # 학습 스킬 (Observability Retro)
├── rules/                   # [제1원칙] 한글 사용 및 코딩 표준
├── mcp/                     # MCP 도구 설정 (mcp_config.json)
├── tools/                   # 슬래시 커맨드 정의 (commands.md)
├── memory/                  # 메타 러닝 저장소 (failures/, lessons/)
├── reports/                 # [NEW] 산출물 저장소 (specs/, verification/)
│   └── recommendations/     # [NEW] 트렌드 추천
├── hooks/                   # [NEW] 자동화 훅 설정 (hooks.json)
└── scripts/
    └── swarm/               # 병렬 에이전트 오케스트레이션 (orchestrator.py)
```

## 5. 훅 시스템 (Hooks System)
Antigravity는 `hooks/hooks.json`에 정의된 자동화 훅을 포함하여 워크플로우를 보조합니다:
- **Session Start**: `memory/lessons/`에서 교훈을 로드하여 컨텍스트를 제공합니다.
- **Session End**: 세션 로그를 `memory/sessions/`에 저장합니다.
- **Pre-Tool Safety**:
    - `git push` 전 검증 리마인더를 표시합니다.
    - 규칙에 어긋나는 무분별한 마크다운 파일 생성을 방지합니다.
- **Quality Checks**: 파일 수정 후 남아있는 `console.log` 감지.

## 6. 실행 모드 (Execution Modes)
Antigravity는 작업 복잡도에 따라 두 가지 모드로 실행할 수 있습니다.

### 6.1 대화형 모드 (Interactive Mode)
**추천**: 일상적인 개발, TDD, 단일 기능 기능.
- **방법**: IDE(Cursor, Windsurf) 채팅창에서 LLM과 대화합니다.
- **실행**: `/plan`, `/tdd` 등의 명령어를 입력합니다.
- **원리**: LLM이 `AGENTS.md` 컨텍스트를 기반으로 에이전트(Planner, Developer) 역할을 수행하며 도구를 실행합니다.

### 6.2 자율 모드 (Autonomous Swarm)
**추천**: 복잡한 마이그레이션, 대규모 리팩토링, 다중 파일 작업.
- **트리거**:
  - **수동**: `python scripts/swarm/orchestrator.py`
  - **자동 (Seamless)**: Planner 에이전트가 `task_plan.md` 승인 후 자동으로 스크립트를 트리거합니다.
- **원리**: 여러 에이전트 인스턴스가 병렬로 실행되며 `checklist`와 `shared_memory`를 통해 소통합니다.

### 6.3 Jules Orchestrator (실험적 기능)
**추천**: Python 스크립트 없이 로직 기반 오케스트레이션이 필요할 때.
- **도구**: `antigravity-jules-orchestration3` (MCP)
- **개념**: MCP 도구를 통해 LLM이 하위 에이전트를 생성하고 관리하는 방식.
- **참고**: 상태 관리를 위해 GitHub 저장소가 필요합니다. 숙련된 사용자에게 권장됩니다.

## 7. 병렬 스웜 및 오케스트레이션 (Parallel Swarm & Orchestration)
(Swarm 구성에 대한 고급 세부 정보...)

### 7.1 병렬 실행 (Parallel Execution)
Swarm Orchestrator를 실행하여 `agents/roles.yaml`에 정의된 에이전트를 병렬/직렬 단계로 실행합니다.
```bash
python scripts/swarm/orchestrator.py
```
이 작업은 다음을 수행합니다:
1.  `agents/roles.yaml`을 읽습니다.
2.  공유 컨텍스트(`task_plan.md` 등)를 주입합니다.
3.  `mode`(병렬/직렬)에 따라 에이전트를 동시에 실행합니다.

### 7.2 Jules 통합 (MCP)
`antigravity-jules-orchestration3` MCP 서버는 `mcp/mcp_config.json`에 설정되어 있습니다. 이를 통해 도구 인터페이스를 통한 고급 오케스트레이션 기능을 사용할 수 있습니다.

### 7.3 Auto-Swarm Skill
복잡한 작업에 대해 자동으로 스웜을 트리거하도록 에이전트를 구성할 수 있습니다.
- **위치**: `skills/common/antigravity-swarm/SKILL.md`
- **조건**: 파일 3개 이상 또는 별도 역할이 필요한 작업.
- **동작**: `planner.py` -> `orchestrator.py` 흐름 자동화.

### 7.4 Vibe Coding Workflow
빠른 반복을 위해 "Think-Run-Feedback" 루프를 엄격히 준수합니다.
- **위치**: `skills/common/vibe-coding/SKILL.md`
- **에이전트**: `Vibe_Coding_Coach`가 짧은 루프를 강제합니다.
- **합성 데이터**: `skills/common/vibe-coding/synthetic_data.md`를 사용하여 테스트 데이터를 즉시 생성합니다.

## 8. MSA 아키텍처
Antigravity는 모듈형 에이전트 아키텍처(MSA)를 따릅니다.
- **규칙**: `rules/msa_architecture.rules.md`
- **원칙**: 서비스로서의 에이전트(Agents as Services), 인프라로서의 MCP.
- **에이전트**: `MCP_Steward`가 도구 레지스트리와 아키텍처 준수를 관리합니다.

## 9. 기여하기 (Contributing)
새로운 스킬을 추가하거나 규칙을 변경하려면 해당 디렉토리의 파일을 수정하고 `agents/workflow.md`에 반영해 주세요.
