# Antigravity 코딩 표준 (Code Standards)

이 문서는 모든 에이전트가 준수해야 할 코드 품질 및 개발 행동 강령을 정의합니다.

## 1. 핵심 원칙 (Core Principles)

### 1.1 불변성 (Immutability)
- **원칙**: 객체나 배열을 직접 수정(Mutation)하지 않고, 항상 새로운 복사본을 생성하여 반환합니다.
- **이유**: 사이드 이펙트를 최소화하고 상태 관리의 예측 가능성을 높이기 위함입니다.
```javascript
// Bad
function updateName(user, name) {
  user.name = name;
  return user;
}

// Good
function updateName(user, name) {
  return { ...user, name };
}
```

### 1.2 Fail-Safe & Error Handling
- **원칙**: 모든 입출력 및 외부 요청에는 철저한 예외 처리를 적용합니다.
- **원칙**: 에러 발생 시 단순 로깅을 넘어, 사용자에게 명확한 원인을 '한글'로 설명해야 합니다.
- **필수**: `try-catch` 블록 내에서 `console.error`로 에러 스택을 출력하고, 심각한 장애는 `memory/failures/`에 기록해야 합니다.

### 1.3 TDD (Test Driven Development)
- **원칙**: 구현 전 테스트 작성을 원칙으로 합니다 (`/tdd` 워크플로우 준수).
- **이유**: 요구사항을 명확히 하고, 리팩토링 안전망을 확보하기 위함입니다.

## 2. 메타 러닝 및 기억 (Meta-Learning & Memory)

### 2.1 실패 기록 (Failure Logging)
- **규칙**: 빌드 실패, 테스트 실패, 런타임 에러 등 **1회 이상 반복된 오류**는 반드시 기록합니다.
- **저장소**: `antigravity-setup/memory/failures/`
- **형식**: `YYYY-MM-DD_error_summary.md`
- **내용**:
  1.  발생 상황 (Context)
  2.  에러 로그 (Raw Output)
  3.  시도한 해결책 (Attempted Fixes)
  4.  최종 원인 분석 (Root Cause)

### 2.2 회고 및 학습 (Retrospection)
- **규칙**: 작업 세션이 종료되거나 하나의 큰 기능(Feature)이 완료되면 `/learn` 명령을 수행합니다.
- **액션**: `memory/failures/`의 로그를 분석하여, 다음 프로젝트에 적용할 '교훈(Instinct)'을 `memory/lessons/`에 저장합니다.

## 3. 문서화 (Documentation)
- **원칙**: 코드는 그 자체로 문서가 되어야 하지만, 복잡한 로직에는 반드시 한글 주석을 첨부합니다.
- **README**: 각 디렉토리 및 모듈에는 해당 역할과 사용법을 설명하는 `README.md`가 존재해야 합니다.
