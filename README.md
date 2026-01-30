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

## 2. Installation & Setup

### 2.1 Prerequisites
- **Node.js** (v18+): Required to run MCP servers.
- **Python** (v3.10+): Recommended when using Python-related skills.
- **Git**: Essential for version control.

### 2.2 Install MCP Servers
Install the necessary packages to activate the tools defined in `mcp/mcp_config.json`.

```bash
# 1. Install MCP server packages (Global or Project local)
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @modelcontextprotocol/server-memory
npm install -g @modelcontextprotocol/server-github
npm install -g @modelcontextprotocol/server-sequential-thinking
```

### 2.3 Environment Variables Configuration
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

## 4. Directory Structure

```
antigravity-setup/
├── agents/                  # Agent roles (roles.yaml) and workflow (workflow.md)
├── skills/                  # Specialized skills by phase (Planning, Design, Implementation, Testing, Learning)
│   ├── specification-writer # [NEW] Spec writing skill
│   └── verification-reporter # [NEW] Verification reporting skill
├── rules/                   # [First Principle] Korean usage and coding standards
├── mcp/                     # MCP tool configuration (mcp_config.json)
├── tools/                   # Slash command definitions (commands.md)
├── memory/                  # Meta-learning storage (failures/, lessons/)
└── reports/                 # [NEW] Output storage (specs/, verification/)
```

## 5. Contributing
To add a new skill or change a rule, modify the file in the appropriate directory and reflect it in `agents/workflow.md`.
