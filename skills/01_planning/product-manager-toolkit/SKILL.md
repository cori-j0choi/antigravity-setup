---
name: product-manager-toolkit
description: 제품 기획, 요구사항 분석, PRD 작성 및 로드맵 수립을 위한 포괄적인 도구 모음입니다.
---

# Product Manager Toolkit

이 스킬은 Antigravity의 **Planner** 에이전트가 고품질의 기획 문서를 작성하도록 돕습니다.

## 1. 사용 시점 (Triggers)
- 새로운 프로젝트나 기능을 시작할 때 (`/plan` 명령어 실행 시).
- 사용자의 요구사항이 모호하여 구체화가 필요할 때.
- 기능의 우선순위를 결정해야 할 때 (P0, P1, P2).

## 2. 핵심 기능 (Capabilities)

### 2.1 요구사항 분석 (Requirements Analysis)
- **목표**: 사용자의 의도를 명확히 파악합니다.
- **활동**:
    - "무엇을", "왜", "누구를 위해" 만드는지 질문합니다.
    - 모호한 표현을 구체적인 수치나 조건으로 변환합니다.

### 2.2 PRD 작성 (Product Requirements Document)
- **포맷**:
    ```markdown
    # [프로젝트명] PRD

    ## 1. 배경 및 목적 (Background & Goals)
    - 해결하고자 하는 문제:
    - 비즈니스 가치:

    ## 2. 타겟 사용자 (Target Audience)
    - 주요 사용자 페르소나:

    ## 3. 유저 스토리 (User Stories)
    - [P0] 사용자는 ... 할 수 있어야 한다.

    ## 4. 기능 명세 (Functional Specs)
    - Feature A: ...
    - Feature B: ...

    ## 5. 비기능 요건 (Non-Functional Requirements)
    - 성능, 보안, 확장성 등
    ```

### 2.3 우선순위 결정 (Prioritization)
- **MoSCoW 기법** 사용:
    - **Must have**: 필수 기능 (MVP).
    - **Should have**: 중요하지만 당장 없어도 되는 기능.
    - **Could have**: 있으면 좋은 기능.
    - **Won't have**: 이번 범위 아님.

## 3. `/plan` 명령어와의 통합
- 이 스킬은 `/plan` 명령어가 실행될 때 자동으로 로드되어, Planner가 체계적으로 계획을 수립하도록 지원합니다.
