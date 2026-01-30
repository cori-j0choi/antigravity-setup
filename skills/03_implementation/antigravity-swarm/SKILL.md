---
name: antigravity-swarm
description: Planner, Architect, Developer 등 다중 에이전트 간의 협업과 오케스트레이션을 정의하는 전문 스킬입니다.
---

# Antigravity Swarm Skill

이 스킬은 **Antigravity Multi-Agent System**의 핵심 오케스트레이션 로직을 정의합니다.

## 1. 에이전트 역할 (Role Definitions)
`agents/roles.yaml`에 정의된 역할들을 준수합니다.

- **Planner (Blue)**: 기획 및 오케스트레이션 헤드.
- **Architect (Magenta)**: 기술적 의사결정 및 설계.
- **Developer (Cyan)**: 실제 구현 (Workhorse).
- **Tester (Yellow)**: 품질 보증 및 검증.
- **Reviewer (Green)**: 최종 관문 (Gatekeeper).

## 2. 워크플로우 (Workflow Integration)
`agents/workflow.md`의 **Manus Protocol**을 따릅니다.

### Phase 1: Planning
- Planner는 `/plan` 명령을 통해 호출됩니다.
- 결과물: `task_plan.md` (사용자 승인 필수).

### Phase 2: Design
- Architect는 `findings.md`에 설계를 기록합니다.
- Developer는 이 문서를 '진실의 원천(Source of Truth)'으로 간주합니다.

### Phase 3: Execution
- Developer와 Tester는 `/tdd` 사이클을 돕니다.
- `progress.md`에 진행상황을 실시간으로 업데이트합니다.

## 3. 오케스트레이션 도구 (Tools)
- **dispatch_subagent**: 특정 역할을 가진 서브 에이전트를 호출하여 임무를 위임합니다.
- **handoff_to**: 현재 작업 컨텍스트를 다른 에이전트에게 전달합니다. (예: Dev -> Tester).

## 4. 커뮤니케이션 규칙
- 모든 에이전트는 **한글**로 의사소통합니다.
- 중요 상태 변경 시 반드시 `progress.md`를 업데이트하여 다른 에이전트에게 알립니다.
