# Antigravity Workflow (Manus Protocol)

Antigravity agents collaborate according to the following protocol.

## 1. Initialization
- **Shared Context**: State is shared via `task_plan.md`, `findings.md`, and `progress.md`.
- **Language Rule**: Follows `00_language.rules.md` (Default: English, Option: Korean).

## 2. Phased Process

### Phase 1: Planning (`/plan`)
- **Owner**: Planner
- **Activities**:
  1.  Analyze user request.
  2.  Refer to `memory/lessons/` for past failure patterns.
  3.  Create `task_plan.md` and request user approval.
  4.  **[/spec]** Create detailed specification (`reports/specs/`).
  5.  **[/trend]** Conduct Trend Radar (`reports/recommendations/`).
- **Exit Condition**: User's explicit Confirmation.

### Phase 2: Design
- **Owner**: Architect
- **Activities**:
  1.  Technical design based on `task_plan.md`.
  2.  Define architecture and schema in `findings.md`.
- **Exit Condition**: Design documentation complete.

### Phase 3: Execution (`/tdd`)
- **Owner**: Developer, Tester
- **Activities**:
  1.  **Red**: Tester writes failing test.
  2.  **Green**: Developer implements minimal code.
  3.  **Refactor**: Developer improves code.
  4.  **Log**: Record `memory/failures/` on failure.
  5.  Update `progress.md`.
- **Exit Condition**: All tests pass (All Green).

### Phase 4: Verification (`/verify`)
- **Owner**: Tester
- **Activities**:
  1.  Perform Build, Test, Lint, Security checks.
  2.  **Report**: Generate verification report in `reports/verification/`.
- **Exit Condition**: All items PASS and report generated.

### Phase 4.1: Evaluation (`/eval`)
- **Owner**: Tester, Reviewer
- **Activities**:
  1.  Perform Regression Benchmarks and LLM Judge evaluation.
  2.  Compare quality metrics and detect degradation.
- **Exit Condition**: Evaluation report generated and Quality Gate passed.

### Phase 4.2: Red Team (`/redteam`)
- **Owner**: Reviewer, Security
- **Activities**:
  1.  Test Prompt Injection and Tool Misuse.
  2.  Generate Vulnerability Report and Mitigation Strategies.
- **Exit Condition**: No critical vulnerabilities or fixes applied.

### Phase 5: Code Review (`/review`)
- **Owner**: Reviewer
- **Activities**:
  1.  Check Verification Report.
  2.  Review Code Quality, Style, and Security.
  3.  Check compliance with `code_standards.md`.
- **Exit Condition**: Reviewer Approval.

### Phase 6: Retrospection (`/learn`)
- **Owner**: All Agents
- **Activities**:
  1.  Retrospective after project completion.
  2.  Analyze `memory/failures/` -> Turn into knowledge in `memory/lessons/`.
  3.  Derive improvements based on observability metrics (Cost, Latency, Quality).
