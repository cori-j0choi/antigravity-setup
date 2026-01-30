---
name: verification-reporter
description: 코드 변경 후 빌드, 테스트, 린트, 보안 검사를 수행하고 그 결과를 상세한 리포트로 생성하는 스킬입니다.
---

# Verification Reporter Skill

이 스킬은 Antigravity의 **Tester** 및 **Reviewer** 에이전트가 코드 품질을 객관적으로 증명하도록 돕습니다.

## 1. 개요 (Overview)
- **목적**: "제대로 만들었는가"를 검증하고 결과를 기록합니다.
- **산출물**: `antigravity-setup/reports/verification/` 디렉토리에 마크다운 파일로 저장됩니다.
- **Trigger**: `/verify` 명령어 사용 시.

## 2. 검증 절차 (Verification Steps)
다음 단계들을 순차적으로 실행하고 결과를 수집합니다.

1.  **Build Check**: 프로젝트 빌드 성공 여부.
2.  **Type Check**: TypeScript/Python 타입 에러 검사.
3.  **Lint Check**: 코드 스타일 및 잠재적 오류 검사.
4.  **Test Suite**: 단위/통합 테스트 실행 및 커버리지 확인.
5.  **Security Scan**: 하드코딩된 비밀 키(Secret)나 취약 함수 사용 여부.

## 3. 리포트 템플릿 (Report Template)

리포트는 `antigravity-setup/reports/verification/[YYYY-MM-DD]_[Feature]_VERIFY.md` 형식으로 저장합니다.

```markdown
# [Feature Name] Verification Report

**Status**: [PASS/FAIL]
**Verifier**: [Agent Name]
**Date**: YYYY-MM-DD HH:MM

## 1. Summary
- **Build**: [PASS/FAIL]
- **Tests**: [X/Y passed] ([Z]% coverage)
- **Lint**: [X warnings]
- **Security**: [Safe/Issues found]

## 2. Detailed Findings
### 2.1 Build & Types
- [로그 요약]

### 2.2 Tests
- [실패한 테스트 케이스 목록]

### 2.3 Lint & Style
- [주요 위반 사항]

## 3. Action Items
- [ ] [수정해야 할 항목 1]
- [ ] [수정해야 할 항목 2]

## 4. Conclusion
- [ ] Ready for Merge
- [ ] Needs Work
```

## 4. 워크플로우
1.  **Run**: `/verify` 명령어로 전체 검사 수행.
2.  **Report**: 결과 리포트 생성 및 저장.
3.  **Review**: Reviewer가 리포트 기반으로 최종 승인 여부 결정.
