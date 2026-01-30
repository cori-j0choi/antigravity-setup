# Antigravity 워크플로우 (Manus Protocol)

Antigravity 에이전트는 다음 프로토콜에 따라 협업합니다.

## 1. 초기화 (Initialization)
- **Shared Context**: `task_plan.md`, `findings.md`, `progress.md` 파일을 통해 상태를 공유합니다.
- **Language Rule**: 모든 의사소통은 `00_language.rules.md`에 따라 **한글**로 진행합니다.

## 2. 단계별 프로세스 (Phased Process)

### Phase 1: Planning (`/plan`)
- **주체**: Planner
- **활동**:
  1.  사용자 요청 분석.
  2.  `memory/lessons/` 참조하여 과거 실패 패턴 확인.
  3.  `task_plan.md` 작성 및 사용자 승인 요청.
  4.  **[/spec]** 상세 명세서 작성 (`reports/specs/`).
  5.  **[/trend]** 트렌드 레이더 수행 (`reports/recommendations/`).
- **종료 조건**: 사용자의 명시적 승인 (Confirmation).

### Phase 2: Design
- **주체**: Architect
- **활동**:
  1.  `task_plan.md` 기반 기술 설계.
  2.  `findings.md`에 아키텍처 및 스키마 정의.
- **종료 조건**: 설계 문서 완료.

### Phase 3: Execution (`/tdd`)
- **주체**: Developer, Tester
- **활동**:
  1.  **Red**: Tester가 실패하는 테스트 작성.
  2.  **Green**: Developer가 최소 구현.
  3.  **Refactor**: Developer가 코드 개선.
  4.  **Log**: 실패 시 `memory/failures/` 기록.
  5.  `progress.md` 업데이트.
- **종료 조건**: 모든 테스트 통과 (All Green).

### Phase 4: Verification (`/verify`)
- **주체**: Tester
- **활동**:
  1.  빌드, 테스트, 린트, 보안 검사 수행.
  2.  **Report**: `reports/verification/`에 검증 리포트 생성.
- **종료 조건**: 모든 항목 PASS 및 리포트 생성 완료.

### Phase 4.1: Evaluation (`/eval`)
- **주체**: Tester, Reviewer
- **활동**:
  1.  회귀 벤치마크 및 LLM Judge 평가 수행.
  2.  품질 지표 비교 및 하락 감지.
- **종료 조건**: 평가 리포트 생성 및 품질 게이트 통과.

### Phase 4.2: Red Team (`/redteam`)
- **주체**: Reviewer, Security
- **활동**:
  1.  프롬프트 인젝션 및 툴 오남용 테스트.
  2.  취약점 리포트 및 완화 방안 도출.
- **종료 조건**: 치명적 취약점 없음 또는 수정 완료.

### Phase 5: Code Review (`/review`)
- **주체**: Reviewer
- **활동**:
  1.  검증 리포트 확인.
  2.  코드 품질, 스타일, 보안 검토.
  2.  `code_standards.md` 준수 여부 확인.
- **종료 조건**: Reviewer 승인.

### Phase 6: Retrospection (`/learn`)
- **주체**: All Agents
- **활동**:
  1.  프로젝트 종료 후 회고.
  2.  `memory/failures/` 분석 -> `memory/lessons/`로 지식화.
  3.  관측성 지표(비용, 지연시간, 품질) 기반 개선안 도출.
