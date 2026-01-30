# Antigravity 도구 및 커맨드 (Tools & Commands)

Antigravity 에이전트는 상황에 맞는 명확한 행동 지침을 `Slash Command` 형태로 제공받습니다.

## 1. 기획 및 계획 (`/plan`)
- **설명**: 새로운 작업이나 기능을 시작할 때 사용합니다. Planner 에이전트를 호출하여 요구사항을 분석하고 실행 계획을 수립합니다.
- **프로세스**:
  1.  요구사항 분석 (Requirements Analysis)
  2.  리스크 평가 (Risk Assessment)
  3.  단계별 계획 수립 (Phased Implementation Plan)
  4.  **[필수] 사용자 승인 대기 (Wait for Confirmation)**

## 2. 명세서 작성 (`/spec`)
- **설명**: 개발 착수 전, 상세한 기술 명세서를 작성합니다. Planner 또는 Architect가 수행합니다.
- **산출물**: `antigravity-setup/reports/specs/[Feature]_SPEC.md`.
- **내용**:
  1.  User Story & Scope.
  2.  Interface Specs (UI/API).
  3.  Data Model & Scenarios.
  4.  Verification Criteria.

## 3. TDD 개발 (`/tdd`)
- **설명**: 실제 구현 단계에서 사용합니다. Developer와 Tester 에이전트가 협업하여 TDD 사이클을 엄격히 준수합니다.
- **프로세스**:
  1.  **Red**: 실패하는 테스트 케이스 작성.
  2.  **Green**: 테스트를 통과하는 최소한의 코드 작성.
  3.  **Refactor**: 코드 구조 개선 및 중복 제거.
  4.  **[Failure Log]**: 구현 중 반복적인 실패 발생 시 `memory/failures/`에 원인 기록.

## 4. 검증 및 리포트 (`/verify`)
- **설명**: 구현된 코드의 품질을 검증하고 리포트를 생성합니다. Tester가 수행합니다.
- **프로세스**:
  1.  **Build Check**: 빌드 성공 여부.
  2.  **Test Suite**: 테스트 통과 및 커버리지 확인.
  3.  **Lint/Security**: 스타일 및 보안 점검.
  4.  **Report**: `antigravity-setup/reports/verification/`에 결과 저장.

## 4.1 품질 평가 (`/eval`)
- **설명**: 회귀 벤치마크와 LLM Judge 평가를 수행합니다.
- **프로세스**:
  1.  Golden Set 및 시나리오 세트 실행.
  2.  정량/정성 지표 종합.
  3.  결과를 `reports/verification/`에 기록.

## 4.2 보안 레드팀 (`/redteam`)
- **설명**: 프롬프트 인젝션 및 툴 오남용을 점검합니다.
- **프로세스**:
  1.  공격 시나리오 테스트.
  2.  취약점 리포트 생성.
  3.  완화 방안 문서화.

## 5. 코드 리뷰 (`/review`)
- **설명**: 구현이 완료된 후, 또는 중간 점검이 필요할 때 사용합니다. Reviewer 에이전트가 코드 품질, 보안, 스타일 준수 여부를 검사합니다.
- **체크리스트**:
  -   `00_language.rules.md` 준수 여부 (한글 사용).
  -   `code_standards.md` 준수 여부 (불변성, 에러 핸들링).
  -   테스트 커버리지 및 통과 여부.

## 6. 학습 및 회고 (`/learn`)
- **설명**: 작업 세션이 종료되거나 프로젝트가 끝났을 때 사용합니다. 실패 로그를 분석하여 교훈을 추출합니다.
- **프로세스**:
  1.  `memory/failures/` 내 로그 분석.
  2.  재발 방지 대책 및 패턴 도출 (Instinct Extraction).
  3.  `memory/lessons/`에 영구적인 지식으로 저장.

## 7. 관측성 체크 (`/observe`)
- **설명**: 비용, 지연시간, 품질 지표를 통합 점검합니다.
- **프로세스**:
  1.  핵심 지표 수집 및 병목 분석.
  2.  개선 우선순위 도출.
  3.  회고 자료로 전달.

## 8. 트렌드 레이더 (`/trend`)
- **설명**: 최신 스킬/도구/MCP 트렌드를 정리합니다.
- **프로세스**:
  1.  신규 도구 및 모델 동향 조사.
  2.  적용 가능성 평가 및 우선순위 설정.
  3.  `reports/recommendations/`에 결과 저장.
