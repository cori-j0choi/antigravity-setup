# Antigravity Setup Guide

**Antigravity**는 LLM 에이전트(Planner, Architect, Developer, Tester, Reviewer)가 유기적으로 협업하며 지속적으로 학습하는 **자율형 개발 환경** 설정입니다.

이 문서는 `antigravity-setup` 패키지의 설치, 설정 및 사용 방법을 안내합니다.

## 1. 개요 (Overview)

이 설정 패키지는 다음 핵심 가치를 제공합니다:
- **Role-Based Collaboration**: 명확한 역할 분담과 책임 정의 (`agents/roles.yaml`).
- **Manus Protocol Implementation**: 체계적인 협업 프로토콜 (`agents/workflow.md`).
- **Korean First**: 모든 문서화 및 소통의 한글화 (`rules/00_language.rules.md`).
- **Meta-Learning**: 실패로부터 배우고 진화하는 파이프라인 (`memory/failures/`, `skills/continuous-learning`).
- **Trend Alignment**: 최신 트렌드 기반 스킬/에이전트 확장 (`reports/recommendations/`).

## 2. 설치 및 설정 (Installation & Setup)

### 2.1 사전 요구사항 (Prerequisites)
- **Node.js** (v18 이상): MCP 서버 실행을 위해 필요합니다.
- **Python** (v3.10 이상): Python 관련 스킬 활용 시 권장됩니다.
- **Git**: 버전 관리를 위해 필수입니다.

### 2.2 MCP 서버 설치
`mcp/mcp_config.json`에 정의된 도구들을 활성화하기 위해 필요한 패키지를 설치합니다.

```bash
# 1. MCP 서버 패키지 설치 (Global 또는 프로젝트 로컬)
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @modelcontextprotocol/server-memory
npm install -g @modelcontextprotocol/server-github
npm install -g @modelcontextprotocol/server-sequential-thinking
```

### 2.3 환경 변수 설정
`mcp_config.json` 또는 시스템 환경 변수에 다음 값을 설정해야 합니다.

- `GITHUB_PERSONAL_ACCESS_TOKEN`: GitHub 저장소 접근 권한이 있는 토큰.

### 2.4 에이전트 설정 연동
사용 중인 LLM 에이전트 시스템(예: Claude Desktop, Custom Agent Runner)에 이 디렉토리를 **Context**로 제공하거나 **Config Path**로 지정해야 합니다.

- **Context Path**: `d:\2026\08_antigravity_everything_code\antigravity-setup`

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
- **[NEW]** `/eval`, `/redteam`, `/observe` 단계를 통해 품질/보안/관측성을 보강합니다.

## 3.5 트렌드 검토 (`/trend`)
메타 파이프라인 품질을 높이기 위해 최신 도구/에이전트/스킬을 점검합니다.

- 결과는 `reports/recommendations/`에 저장합니다.

## 4. 디렉토리 구조 (Directory Structure)

```
antigravity-setup/
├── agents/                  # 에이전트 역할(roles.yaml) 및 워크플로우(workflow.md)
├── skills/                  # 단계별 전문 스킬 (기획, 설계, 구현, 테스트, 학습)
│   ├── 01_planning/          # 트렌드 레이더 등 기획 스킬
│   ├── 03_implementation/    # Tool Reliability 등 구현 스킬
│   ├── 04_testing/           # Evals, Red-Teaming 스킬
│   └── 05_learning/          # Observability 기반 회고 스킬
├── rules/                   # [제1원칙] 한글 사용 및 코딩 표준
├── mcp/                     # MCP 도구 설정 (mcp_config.json)
├── tools/                   # 슬래시 커맨드 정의 (commands.md)
├── memory/                  # 메타 러닝 저장소 (failures/, lessons/)
└── reports/                 # [NEW] 산출물 저장소 (specs/, verification/)
    └── recommendations/     # [NEW] 트렌드 제안서
```

## 5. 기여 (Contributing)
새로운 스킬을 추가하거나 규칙을 변경하려면 해당 디렉토리의 파일을 수정하고, `agents/workflow.md`에 반영해 주세요.
