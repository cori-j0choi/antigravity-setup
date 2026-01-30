---
name: clean-code
description: 가독성 높고, 유지보수 용이하며, 버그를 최소화하는 클린 코드 작성 원칙입니다.
---

# Clean Code Skill

이 스킬은 Antigravity의 모든 에이전트가 고품질의 코드를 생산하도록 가이드합니다.

## 1. 네이밍 (Naming)
- **의도를 명확히**: 변수명, 함수명만 보고도 역할이 드러나야 합니다.
    - `d` (X) -> `elapsedDays` (O)
    - `check` (X) -> `validateUserPermissions` (O)
- **일관성**: 프로젝트 전반에 걸쳐 동일한 용어를 사용합니다 (e.g., `fetch` vs `get` vs `retrieve`).

## 2. 함수 (Functions)
- **작게 만들기**: 함수는 하나의 기능만 수행해야 합니다. 20줄을 넘지 않도록 노력하세요.
- **인수 최소화**: 3개 이상의 인수가 필요하면 객체(Object)를 전달하는 것을 고려하세요.
- **Side Effect 방지**: 함수 내부에서 외부 상태를 변경하지 않도록 합니다 (순수 함수 지향).

## 3. 주석 (Comments)
- **코드로 설명**: 주석 없이 코드만으로 이해할 수 있는 것이 최선입니다.
- **필요한 주석**: "왜(Why)" 이렇게 구현했는지에 대한 의도나, 복잡한 비즈니스 로직에 대한 설명을 한글로 작성합니다.
- **불필요한 주석**: "무엇을(What)" 하는지 설명하는 중복 주석은 지양합니다.

## 4. 리팩토링 (Refactoring) - `/tdd`
- **TDD Cycle**: Make it work (Green) -> Make it right (Refactor).
- **Boy Scout Rule**: 코드를 건드릴 때마다, 처음보다 더 깨끗하게 만들어 놓고 떠납니다.
- **중복 제거**: DRY(Don't Repeat Yourself) 원칙 준수.

## 5. 에러 처리 (Error Handling)
- **우아한 실패**: 예외를 무시하지 말고(swallowing), 적절히 포착하여 처리하거나 로깅합니다.
- **null 반환 지양**: 가능하면 Null Object Pattern이나 Optional 타입을 사용합니다.
