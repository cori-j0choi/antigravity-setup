---
name: continuous-learning
description: 에이전트의 경험(성공/실패)을 분석하여 재사용 가능한 Instinct(직관)로 변환하고 저장하는 메타 러닝 스킬입니다.
---

# Continuous Learning Skill (Homonculus Inspired)

이 스킬은 Antigravity 에이전트가 **경험으로부터 학습**하고 스스로 진화할 수 있도록 합니다.

## 1. 메타 러닝 파이프라인 (Meta-Learning Pipeline)

### Step 1: 관찰 (Observation)
- 에이전트의 모든 활동(Tool Usage, Error Logs)을 모니터링합니다.
- 특히 **사용자의 수정 요청**이나 **반복되는 에러**는 중요한 학습 신호입니다.

### Step 2: 추출 (Extraction - `/learn`)
- 세션 종료 후 또는 실패 직후 `/learn` 명령을 통해 패턴을 추출합니다.
- **Instinct Model**:
    - `Trigger`: 언제 이 패턴을 적용해야 하는가?
    - `Action`: 무엇을 해야 하는가?
    - `Confidence`: 이 패턴에 대한 확신 수준 (0.0 ~ 1.0).

### Step 3: 저장 (Storage)
- 추출된 Instinct는 `memory/lessons/` 디렉토리에 저장됩니다.
- 형식:
    ```markdown
    # Instinct: [Pattern Name]
    - **Context**: [상황 설명]
    - **Solution**: [해결 방법]
    - **Origin**: [실패 로그 링크]
    ```

### Step 4: 적용 (Application)
- **Planning** 단계에서 `/plan` 실행 시, Planner는 `memory/lessons/`를 먼저 스캔합니다.
- 과거의 실패 패턴과 유사한 상황이 감지되면, 사전에 경고하고 계획에 반영합니다.

## 2. 명령어 (Commands)
- `/instinct-status`: 현재 활성화된 Instinct 목록 확인.
- `/instinct-import`: 외부 지식이나 동료 에이전트의 Instinct 가져오기.
- `/evolve`: 축적된 Instinct들을 일반화하여 새로운 Skill이나 Rule로 승격.

## 3. 실패 기록 연동
- 심각한 실패 발생 시 `ops-troubleshooter`와 연동하여 `memory/failures/`에 기록하고, 이를 즉시 학습 파이프라인에 태웁니다.
