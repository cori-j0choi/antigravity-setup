# Antigravity Tools & Commands

Antigravity agents receive clear behavioral guidelines in the form of `Slash Commands`.

## 1. Planning (`/plan`)
- **Description**: Used when starting a new task or feature. Calls the Planner agent to analyze requirements and create an execution plan.
- **Process**:
  1.  Requirements Analysis
  2.  Risk Assessment
  3.  Phased Implementation Plan
  4.  **[Required] Wait for User Confirmation**

## 2. Specification (`/spec`)
- **Description**: Creates a detailed technical specification before development begins. Performed by Planner or Architect.
- **Artifact**: `projects/reports/specs/[Feature]_SPEC.md`.
- **Content**:
  1.  User Story & Scope
  2.  Interface Specs (UI/API)
  3.  Data Model & Scenarios
  4.  Verification Criteria

## 3. TDD Development (`/tdd`)
- **Description**: Used during the implementation phase. Developer and Tester agents collaborate to strictly follow the TDD cycle.
- **Process**:
  1.  **Red**: Write a failing test case.
  2.  **Green**: Write minimal code to pass the test.
  3.  **Refactor**: Improve code structure and remove duplication.
  4.  **[Failure Log]**: Record cause in `memory/failures/` if repeated failures occur.

## 4. Verification & Reporting (`/verify`)
- **Description**: Verifies the quality of implemented code and generates a report. Performed by Tester.
- **Process**:
  1.  **Build Check**: Verify build success.
  2.  **Test Suite**: Verify test pass and coverage.
  3.  **Lint/Security**: Style and security check.
  4.  **Report**: Save results in `reports/verification/`.

## 4.1 Quality Evaluation (`/eval`)
- **Description**: Performs regression benchmarks and LLM Judge evaluations.
- **Process**:
  1.  Run Golden Set and Scenario Sets.
  2.  Synthesize quantitative/qualitative metrics.
  3.  Record results in `reports/verification/`.

## 4.2 Security Red Team (`/redteam`)
- **Description**: Checks for prompt injection and tool misuse.
- **Process**:
  1.  Test attack scenarios.
  2.  Generate vulnerability report.
  3.  Document mitigation strategies.

## 5. Code Review (`/review`)
- **Description**: Used after implementation or for interim checks. Reviewer agent inspects code quality, security, and style.
- **Checklist**:
  -   Compliance with `00_language.rules.md` (Language preference).
  -   Compliance with `code_standards.md` (Immutability, Error Handling).
  -   Test coverage and pass status.

## 6. Learning & Retrospection (`/learn`)
- **Description**: Used when a session ends or a project completes. Analyzes failure logs to extract lessons.
- **Process**:
  1.  Analyze logs in `memory/failures/`.
  2.  Derive prevention measures and patterns (Instinct Extraction).
  3.  Save as permanent knowledge in `memory/lessons/`.

## 7. Observability Check (`/observe`)
- **Description**: Integrated check of cost, latency, and quality metrics.
- **Process**:
  1.  Collect key metrics and analyze bottlenecks.
  2.  Derive improvement priorities.
  3.  Deliver as retrospective material.

## 8. Trend Radar (`/trend`)
- **Description**: Summarizes latest trends in Skills/Tools/MCPs.
- **Process**:
  1.  Survey new tool and model trends.
  2.  Evaluate applicability and set priorities.
  3.  Save results in `reports/recommendations/`.
