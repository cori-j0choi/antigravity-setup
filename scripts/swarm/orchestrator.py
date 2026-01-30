import yaml
import sys
import subprocess
import threading
import time
import os
import shutil
# Check if rich is installed, if not, handle gracefully or require it
try:
    from rich.console import Console
    from rich.live import Live
    from rich.table import Table
except ImportError:
    print("Error: 'rich' library is required. Install it via 'pip install rich'")
    sys.exit(1)

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../"))
CONFIG_FILE = os.path.join(ROOT_DIR, "agents", "roles.yaml")
DISPATCH_SCRIPT = os.path.join(SCRIPT_DIR, "dispatch_agent.py")

class SubAgentRunner:
    def __init__(self, name, prompt, color, model="auto-gemini-3", mode="parallel"):
        self.name = name
        self.prompt = prompt
        self.color = color
        self.model = model
        self.mode = mode  # parallel, serial, validator
        self.status = "Pending"
        self.log_file = os.path.join(ROOT_DIR, "memory", "logs", f"{name.lower().replace(' ', '_')}.log")
        self.last_log = ""
        self.is_running = False
        self.log_handle = None
        
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    def run(self):
        self.is_running = True
        self.status = "Starting..."
        
        cmd = [
            sys.executable, 
            DISPATCH_SCRIPT, 
            self.prompt,
            "--log-file", 
            self.log_file,
            "--model",
            self.model
        ]
        
        try:
            self.process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.status = "Running"
            
            while self.process.poll() is None:
                self._read_new_logs()
                time.sleep(0.1)
                
            self.status = "Completed" if self.process.returncode == 0 else "Failed"
            self._read_new_logs()
            
        except Exception as e:
            self.status = f"Error: {str(e)}"
        finally:
            self.is_running = False
            if self.log_handle:
                self.log_handle.close()

    def _read_new_logs(self):
        if not self.log_handle:
            if os.path.exists(self.log_file):
                try:
                    self.log_handle = open(self.log_file, 'r', encoding='utf-8', errors='replace')
                except:
                    pass
        
        if self.log_handle:
            try:
                lines = self.log_handle.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    if last_line:
                        self.last_log = last_line
            except:
                pass

def generate_table(runners):
    table = Table(title="Antigravity Swarm Orchestrator", expand=True)
    table.add_column("Agent", style="bold white")
    table.add_column("Mode", style="cyan")
    table.add_column("Status", style="dim")
    table.add_column("Latest Activity", style="italic")

    current_mode = None
    for runner in runners:
        if current_mode is not None and current_mode != runner.mode:
             table.add_section()
        current_mode = runner.mode

        status_style = "green" if runner.status == "Completed" else "yellow" if runner.status == "Running" else "red" if "Error" in runner.status else "white"
        
        status_text = runner.status
        if runner.status == "Running":
            status_text = f"🔄 {runner.status}"
        elif runner.status == "Completed":
            status_text = f"✅ {runner.status}"
            
        table.add_row(
            f"[{runner.color}]{runner.name}[/{runner.color}]",
            runner.mode,
            f"[{status_style}]{status_text}[/{status_style}]", 
            runner.last_log[-50:] if len(runner.last_log) > 50 else runner.last_log
        )
    return table

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if not os.path.exists(CONFIG_FILE):
        print(f"Error: {CONFIG_FILE} not found.")
        return

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Shared Context Injection from memory/task files
    manus_context = "\n\n[SHARED STATE]"
    files_to_inject = ["task_plan.md", "findings.md", "progress.md"]
    for fname in files_to_inject:
        fpath = os.path.join(ROOT_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                manus_context += f"\n--- {fname} ---\n{f.read()}"
    
    manus_context += "\n[END SHARED STATE]\n"
    manus_context += "Instructions: You are part of the Antigravity Swarm. Read the shared state. Update files using <<WRITE_FILE>>."

    runners = []
    parallel_runners = []
    serial_runners = []
    validator_runners = []

    for agent_cfg in config.get('subagents', []):
        full_prompt = agent_cfg['prompt'] + manus_context
        name = agent_cfg['name']
        mode = agent_cfg.get('mode', 'parallel')
        
        runner = SubAgentRunner(
            name, 
            full_prompt, 
            agent_cfg.get('color', 'white'),
            agent_cfg.get('model', 'auto-gemini-3'),
            mode
        )
        
        if mode == 'validator':
            validator_runners.append(runner)
        elif mode == 'serial':
            serial_runners.append(runner)
        else:
            parallel_runners.append(runner)

    runners = parallel_runners + serial_runners + validator_runners

    print("\n[Orchestrator] Swarm Assembled:")
    print(f"{'Name':<20} {'Mode':<10}")
    print("-" * 35)
    for runner in runners:
        print(f"{runner.name:<20} {runner.mode:<10}")
    print("-" * 35)

    if "--yes" not in sys.argv:
        try:
            confirm = input("\nExecute Swarm? [y/N]: ").strip().lower()
            if confirm != 'y': return
        except: pass

    console = Console()
    with Live(generate_table(runners), refresh_per_second=4, console=console) as live:
        # Phase 1: Parallel
        threads = []
        for runner in parallel_runners:
            t = threading.Thread(target=runner.run)
            t.start()
            threads.append(t)
        
        while any(t.is_alive() for t in threads):
            live.update(generate_table(runners))
            time.sleep(0.5)

        # Phase 2: Serial
        for runner in serial_runners:
            t = threading.Thread(target=runner.run)
            t.start()
            while t.is_alive():
                live.update(generate_table(runners))
                time.sleep(0.5)
            
        # Phase 3: Validator
        for runner in validator_runners:
            t = threading.Thread(target=runner.run)
            t.start()
            while t.is_alive():
                live.update(generate_table(runners))
                time.sleep(0.5)
        
        live.update(generate_table(runners))

    print("\nSwarm Execution Complete.")

if __name__ == "__main__":
    main()
