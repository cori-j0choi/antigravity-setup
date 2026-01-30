import sys
import subprocess
import re
import os
import shutil

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../"))
# Use memory for dynamic configurations
CONFIG_FILE = os.path.join(ROOT_DIR, "memory", "swarm_agents.yaml")
DISPATCH_SCRIPT = os.path.join(SCRIPT_DIR, "dispatch_agent.py")

def get_gemini_path():
    path = os.environ.get("GEMINI_PATH")
    if path and os.path.isfile(path): return path
    path = shutil.which("gemini")
    return path

def generate_prompt(mission):
    return f"""
You are a Principal Software Architect and Team Lead.
Your goal is to hire a squad of specialized sub-agents to complete the following mission:
"{mission}"

Rules for hiring:
1. Identify 2-5 distinct roles needed (e.g., frontend, backend, reviewer).
2. For each role, define a clear, specialized system prompt.
3. Assign a unique color (green, yellow, blue, magenta, cyan, red).
4. Assign model 'auto-gemini-3'.
5. [CRITICAL] The FINAL agent MUST be 'Quality_Validator' (mode: validator).
   - Responsibilities: Verify all work, output final report.
6. Execution mode: 'parallel' (default) or 'serial'.

Output Format:
Output ONE single YAML block enclosed in triple backticks (```yaml).
Structure:

subagents:
  - name: "Agent-Name"
    description: "Short description"
    color: "color_name"
    model: "auto-gemini-3"
    mode: "parallel" # or "serial" / "validator"
    prompt: |
      You are [Role].
      [Instructions...]

Do not include any other text.
"""

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python scripts/swarm/planner.py <mission_description>")
        sys.exit(1)

    mission = " ".join(sys.argv[1:])
    print(f"[Planner] Analyzing mission: '{mission}'...")

    gemini_path = get_gemini_path()
    if not gemini_path:
        print("Error: 'gemini' executable not found.")
        sys.exit(1)

    full_prompt = generate_prompt(mission)

    try:
        process = subprocess.run(
            [gemini_path, "chat", full_prompt],
            capture_output=True, text=True, encoding='utf-8'
        )
        
        output = process.stdout
        yaml_match = re.search(r"```yaml\n(.*?)\n```", output, re.DOTALL)
        
        if yaml_match:
            yaml_content = yaml_match.group(1)
            # Enforce auto-gemini-3
            yaml_content = re.sub(r"gemini-\d+\.\d+[-\w]*", "auto-gemini-3", yaml_content)

            # Plan Match (Optional if main planner output produces plan text)
            # For simplicity, we assume the planner just outputs YAML or we could ask for plan too.
            # But the 'skill' pattern implies planner creates the TEAM, and the Team creates the plan.
            # Let's write the YAML config.
            
            os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                f.write(yaml_content)
                
            print(f"[Planner] Team configuration saved to {CONFIG_FILE}.")
            print(f"[Planner] Run: python scripts/swarm/orchestrator.py --config {CONFIG_FILE}")
            
        else:
            print("[Planner] Error: Could not parse YAML from agent output.")
            print(output)
            sys.exit(1)

    except Exception as e:
        print(f"[Planner] Critical Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
