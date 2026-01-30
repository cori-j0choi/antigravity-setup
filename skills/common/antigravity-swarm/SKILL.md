# Skill: Antigravity Swarm (Auto-Triggered)

## Description
This skill enables the agent to autonomously spawn a squad of specialized sub-agents to handle complex, multi-file, or parallelizable tasks.

## Protocol
**Protocol**: This skill **MUST** be considered for any **complex mission**.

### Trigger Conditions
IF the task involves:
- **>3 Files** to create or modify.
- **Distinct Expertise** required (e.g., "Need Backend AND Frontend").
- **Parallel Execution** benefits (e.g., "Write 5 unit tests simultaneously").

### Execution Steps
1.  **Stop** manual execution. Do not try to edit files yourself one by one.
2.  **Plan**: Run the Swarm Planner to hire a team.
    ```bash
    python scripts/swarm/planner.py "[Mission Description]"
    ```
    - Output: `memory/swarm_agents.yaml` will be created.
3.  **Execute**: Run the Swarm Orchestrator with the generated config.
    ```bash
    python scripts/swarm/orchestrator.py --config "memory/swarm_agents.yaml"
    ```
    - This will launch sub-agents in parallel.
4.  **Report**: The final agent (`Quality_Validator`) or the Orchestrator logs will provide the result. Summarize this to the user.
