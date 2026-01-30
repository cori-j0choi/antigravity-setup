---
name: test-automator
description: TDD, 자동화된 테스트, 품질 보증(QA)을 수행하는 전문가 스킬입니다.
---

# Test Automator Skill

이 스킬은 Antigravity의 **Tester** 및 **Developer** 에이전트가 완벽한 테스트 커버리지를 달성하도록 돕습니다.

## 1. TDD 워크플로우 (`/tdd`)
- **Red**: 실패하는 테스트를 먼저 작성합니다. 요구사항을 명확히 하는 단계입니다.
- **Green**: 테스트를 통과하기 위한 최소한의 코드를 작성합니다.
- **Refactor**: 테스트를 유지하면서 코드를 개선합니다.

## 2. 테스트 피라미드 (Test Pyramid)

### 2.1 Unit Tests (70%)
- 개별 함수나 클래스의 동작을 검증합니다.
- **Tools**: Jest, Pytest.
- **Mocking**: 외부 의존성(DB, API)은 반드시 모킹(Mocking)하여 격리합니다.

### 2.2 Integration Tests (20%)
- 여러 모듈이 함께 동작하는지 검증합니다.
- DB나 API와의 실제 연동을 포함할 수 있습니다 (Docker Compose 활용).

### 2.3 E2E Tests (10%)
- 사용자 관점에서 전체 시스템 흐름을 검증합니다.
- **Tools**: Playwright, Cypress.
- **Critical Path**: 로그인, 결제 등 핵심 시나리오 위주로 작성합니다.

## 3. 테스트 자동화 (Automation)
- **CI/CD 통합**: 코드가 푸시될 때마다 자동으로 테스트가 실행되어야 합니다 (GitHub Actions).
- **Pre-commit Hook**: 커밋 전 로컬에서 테스트 및 린트를 강제합니다 (Husky, Pre-commit).

## 4. 실패 분석 (Failure Analysis)
- 테스트 실패 시 로그를 상세히 분석하고 `memory/failures/`에 기록하여 회고 시 활용합니다.
