# Rule: Modular Agent Architecture (MSA)

## Philosophy
Antigravity treats **Agents** and **MCP Servers** as Microservices.
To maximize LLM potential, we decouple capabilities into discrete, focused units.

## Guidelines

### 1. Agents as Services
- Each Agent (defined in `roles.yaml`) should have a **Single Responsibility**.
- **Do not** create "God Agents" that do everything.
- Use the **Swarm** pattern (`scripts/swarm/`) to orchestrate multiple specialized agents.

### 2. MCP as Infrastructure
- **MCP Servers** are the "Backend" of the agent system.
- Tools should be grouped by domain (e.g., `filesystem`, `github`, `search`) into separate servers.
- **Vibe Check**: If a tool config (`mcp_config.json`) gets too large (>10 tools per server), split it.

### 3. Context Separation
- **Context Hygiene**: Agents should only receive the context relevant to their specific task.
- Use `context7` or similar logic to "resolve" dependencies dynamically rather than dumping everything.
- **Reset**: Clear agent memory after a distinct unit of work (Task Boundary).

### 4. Interface Standardization
- All Agents communication via **Markdown Artifacts** (`task_plan.md`, `findings.md`).
- All Tools must have clear **Schema Definitions** (JSON Schema).
