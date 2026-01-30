---
name: concise-planning
description: 복잡한 작업을 실행 가능한 체크리스트로 쪼개고, 리스크를 평가하며, 사용자 승인 절차를 강제하는 기획 스킬입니다.
---

# Concise Planning Skill

이 스킬은 Antigravity의 **Planner** 에이전트가 `task_plan.md`를 효율적으로 작성하도록 돕습니다.

## 1. 사용 시점 (Triggers)
- `/plan` 명령어 실행 시.
- 작업이 3개 이상의 하위 스텝으로 나뉠 때.
- 10분 이상 걸릴 것으로 예상되는 작업 시작 전.

## 2. 프로세스 (Process)

### Step 1: 작업 분해 (Breakdown)
- 작업을 원자적 단위(Atomic Unit)로 분해합니다.
- 각 단위는 구체적인 행동(Action)과 검증 가능한 결과(Output)를 포함해야 합니다.

### Step 2: 리스크 평가 (Risk & Impact)
- 변경 사항이 미칠 영향을 예측합니다.
- **Breaking Changes**: 기존 기능에 영향을 줄 가능성 확인.
- **Security Check**: 보안 취약점 발생 가능성 확인.

### Step 3: 계획서 작성 (`task_plan.md`)
```markdown
# [Project Name] Implementation Plan

## 1. Goal
- [목표를 한 문장으로 요약]

## 2. Key Changes
- [주요 변경 사항 1]
- [주요 변경 사항 2]

## 3. Risks & Considerations
- [리스크 1] (대응 방안: ...)

## 4. Execution Steps
- [ ] Requirements Analysis
- [ ] Phase 1: Core Implementation
    - [ ] Step 1.1: ...
    - [ ] Step 1.2: ...
- [ ] Phase 2: Testing & Verification
    - [ ] Step 2.1: ...
```

### Step 4: 사용자 승인 (Wait for Confirmation)
- **[CRITICAL]** 계획서 작성 후 반드시 사용자의 명시적 승인(`Y`, `Proceed`, `승인`)을 받아야 합니다.
- 승인 없이는 어떠한 코드 변경도 시작해서는 안 됩니다.

## 3. Best Practices
- **간결함 유지**: 불필요한 서술을 줄이고 가독성을 높입니다.
- **한글 작성**: 모든 계획 내용은 `00_language.rules.md`에 따라 한글로 작성합니다.
