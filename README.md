[한국어 (Korean)](README.ko.md)

# Antigravity Setup Guide

**Antigravity** is an **autonomous development environment** setup where LLM agents (Planner, Architect, Developer, Tester, Reviewer) collaborate organically and continuously learn.

This document guides you through the installation, configuration, and usage of the `antigravity-setup` package.

## 1. Overview

This setup package provides the following core values:
- **Role-Based Collaboration**: Clear role division and responsibility definition (`agents/roles.yaml`).
- **Manus Protocol Implementation**: Systematic collaboration protocol (`agents/workflow.md`).
- **Language flexibility**: English by default, with an option for Korean (`rules/00_language.rules.md`).
- **Meta-Learning**: A pipeline that learns from failures and evolves (`memory/failures/`, `skills/continuous-learning`).
- **Trend Alignment**: Trend-based skill/agent expansion (`reports/recommendations/`).

## 2. Installation & Setup

### 2.1 Prerequisites
- **Node.js** (v18+): Required to run MCP servers.
- **Python** (v3.10+): Recommended when using Python-related skills.
- **Git**: Essential for version control.

### 2.2 Install via NPX (Recommended)
This is the easiest way to get started. It clones the repository and sets up the environment.

```bash
# Installs to ~/.agent/antigravity-setup by default
npx antigravity-setup

# Or specify a custom directory
npx antigravity-setup ./my-antigravity
```

### 2.3 Manual Installation
If you prefer to clone manually:

```bash
git clone https://github.com/cori-j0choi/antigravity-setup.git
cd antigravity-setup
npm install
```

### 2.4 Environment Variables Configuration
You need to set the following values in `mcp_config.json` or system environment variables.

- `GITHUB_PERSONAL_ACCESS_TOKEN`: Token with access rights to GitHub repositories.

### 2.4 Agent Configuration Integration
You must provide this directory as **Context** or specify it as **Config Path** in your LLM agent system (e.g., Claude Desktop, Custom Agent Runner).

- **Context Path**: `d:\2026\08_antigravity_everything_code\antigravity-setup`

## 3. Usage Guide

### 3.1 Start a Project (`/plan`)
Call the Planner when developing a new feature or starting a project.

```
/plan [Project Name] [Requirements Description]
```

- Planner reviews `memory/lessons/` and creates a `task_plan.md` reflecting past lessons.
- **[NEW]** You can also write a detailed specification via the `/spec` command.
- Proceed to the next step only after user **Confirmation**.

### 3.2 Implementation & Test (`/tdd`)
Once the design is complete, the Developer and Tester start implementation.

```
/tdd [Feature Name]
```

- **Red**: Write a failing test.
- **Green**: Implement the feature.
- **Refactor**: Improve code.
- If an error occurs during implementation, it is automatically recorded in `memory/failures/`.

### 3.3 Verify & Report (`/verify`)
Verify the quality once the implementation is complete.

```
/verify
```

- Performs build, test, lint, and security checks and generates a report in `reports/verification/`.

### 3.4 Retrospection & Learning (`/learn`)
Extract and save lessons when the work is done.

```
/learn
```

- Analyzes failure logs and saves them as permanent knowledge (Instinct) in `memory/lessons/`.
- **[NEW]** `/eval`, `/redteam`, `/observe` steps reinforce Quality/Security/Observability.

### 3.5 Trend Radar (`/trend`)
Examines latest tools/agents/skills to improve meta-pipeline quality.

- Results are saved in `reports/recommendations/`.

## 4. Directory Structure

```
antigravity-setup/
├── agents/                  # Agent roles (roles.yaml) and workflow (workflow.md)
├── skills/                  # Specialized skills by phase
│   ├── 01_planning/         # Planning skills (Trend Radar, etc.)
│   ├── 03_implementation/   # Implementation skills (Tool Reliability, etc.)
│   ├── 04_testing/          # Testing skills (Evals, Red-Team)
│   └── 05_learning/         # Learning skills (Observability Retro)
├── rules/                   # [First Principle] Korean usage and coding standards
├── mcp/                     # MCP tool configuration (mcp_config.json)
├── tools/                   # Slash command definitions (commands.md)
├── memory/                  # Meta-learning storage (failures/, lessons/)
├── reports/                 # [NEW] Output storage (specs/, verification/)
│   └── recommendations/     # [NEW] Trend recommendations
└── hooks/                   # [NEW] Automated workflow hooks (hooks.json)
```

## 5. Hooks System
Antigravity includes automated hooks configured in `hooks/hooks.json` to assist your workflow:
- **Session Start**: Loads context from `memory/lessons/`.
- **Session End**: Saves session logs to `memory/sessions/`.
- **Pre-Tool Safety**:
    - Warnings before `git push` (reminds to verify).
    - Prevents creation of unorganized markdown files.
- **Quality Checks**: Detects `console.log` leftovers after file edits.

## 6. Parallel Swarm & Orchestration
Antigravity supports parallel agent execution for complex tasks.

### 6.1 Parallel Execution (Swarm)
Run the Swarm Orchestrator to execute agents defined in `agents/roles.yaml` in parallel/serial phases.
```bash
python scripts/swarm/orchestrator.py
```
This will:
1.  Read `agents/roles.yaml`.
2.  Inject shared context (`task_plan.md`, etc.).
3.  Run agents concurrently based on their `mode` (parallel/serial).

### 6.2 Jules Integration (MCP)
The `antigravity-jules-orchestration3` MCP server is configured in `mcp/mcp_config.json`. This enables advanced orchestration capabilities directly through the tool interface.

### 6.3 Auto-Swarm Skill
You can configure your agent to automatically trigger the swarm for complex tasks.
- **Location**: `skills/common/antigravity-swarm/SKILL.md`
- **Trigger**: Tasks involving >3 files or distinct roles.
- **Action**: Automates `planner.py` -> `orchestrator.py` flow.

## 7. Contributing
To add a new skill or change a rule, modify the file in the appropriate directory and reflect it in `agents/workflow.md`.
