---
name: specification-writer
description: 개발 착수 전, 상세한 기술 명세서(Specification)를 작성하여 목표를 명확히 하고 오해를 방지하는 스킬입니다.
---

# Specification Writer Skill

이 스킬은 Antigravity의 **Planner** 및 **Architect** 에이전트가 개발 전에 명확한 청사진을 그리도록 돕습니다.

## 1. 개요 (Overview)
- **목적**: "무엇을 만들 것인가"를 코딩 전에 명확히 정의합니다.
- **산출물**: `antigravity-setup/reports/specs/` 디렉토리에 마크다운 파일로 저장됩니다.
- **Trigger**: `/spec` 명령어 사용 시.

## 2. 명세서 템플릿 (Spec Template)

명세서는 `antigravity-setup/reports/specs/[FeatureName]_SPEC.md` 형식으로 저장합니다.

```markdown
# [Feature Name] Specification

**Status**: [Draft/Review/Approved]
**Author**: [Agent Name]
**Date**: YYYY-MM-DD

## 1. 개요 (Overview)
- **User Story**: 사용자는 [목적]을 위해 [기능]을 사용할 수 있다.
- **Scope**: 포함되는 범위와 제외되는 범위를 명확히 기술.

## 2. 인터페이스 명세 (Interface Specs)
### 2.1 UI Components
- [컴포넌트명]: [동작 설명], [제약 조건]

### 2.2 API Endpoints
- `GET /api/resource`: [Request/Response 예시]

## 3. 데이터 모델 (Data Model)
- [Table/Collection 명]: [필드 타입 및 제약조건]

## 4. 시나리오 (Scenarios)
- **Happy Path**: 정상적인 흐름.
- **Edge Cases**: 예외 상황 처리 (네트워크 오류, 잘못된 입력 등).

## 5. 검증 기준 (Verification Criteria)
- [ ] 기준 1
- [ ] 기준 2
```

## 3. 워크플로우
1.  **Draft**: Planner가 초안 작성.
2.  **Review**: 사용자 및 Architect 검토.
3.  **Approve**: 승인 후 개발 착수.
