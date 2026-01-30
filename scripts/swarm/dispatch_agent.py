import sys
import subprocess
import re
import os
import shutil
import json
import time

def parse_and_execute_side_effects(output):
    write_pattern = re.compile(r'<<WRITE_FILE path="([^"]+)">>(.*?)<<END_WRITE>>', re.DOTALL)
    run_pattern = re.compile(r'<<RUN_COMMAND>>(.*?)<<END_COMMAND>>', re.DOTALL)

    for match in write_pattern.finditer(output):
        path = match.group(1)
        content = match.group(2).strip()
        if content.startswith('\n'): content = content[1:]
        if content.endswith('\n'): content = content[:-1]
        
        try:
            # Detect relative vs absolute path. If relative, assume relative to ROOT_DIR ideally, 
            # but current CWD is .../antigravity-setup/ if run from there.
            # We'll just trust the path for now or ensure it's absolute if needed.
            if not os.path.isabs(path):
                # Try to resolve relative to current working directory
                pass

            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[Shim] Wrote to {path}")
        except Exception as e:
            print(f"[Shim] Error writing to {path}: {e}")

    for match in run_pattern.finditer(output):
        command = match.group(1).strip()
        print(f"[Shim] Executing: {command}")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(f"[Shim] Output:\n{result.stdout}")
        except Exception as e:
            print(f"[Shim] Error executing: {e}")

def get_gemini_path():
    path = os.environ.get("GEMINI_PATH")
    if path and os.path.isfile(path): return path
    path = shutil.which("gemini")
    return path

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if len(sys.argv) < 2: return

    gemini_path = get_gemini_path()
    if not gemini_path:
        print("Error: 'gemini' executable not found.")
        sys.exit(1)

    args = sys.argv[1:]
    log_file, model_name = None, "auto-gemini-3"
    
    if "--log-file" in args:
        idx = args.index("--log-file")
        log_file = args[idx+1]
        del args[idx:idx+2]
    
    if "--model" in args:
        idx = args.index("--model")
        model_name = args[idx+1]
        del args[idx:idx+2]

    task = " ".join(args)
    
    shim_instruction = (
        "You are an agent in Antigravity Swarm. "
        "Use <<WRITE_FILE path='...'>>content<<END_WRITE>> to save files. "
        "Use <<RUN_COMMAND>>cmd<<END_COMMAND>> to run shell commands. "
        "Task:\n"
    )
    full_prompt = f"{shim_instruction}{task}"

    log_file_handle = open(log_file, 'a', encoding='utf-8') if log_file else None

    try:
        cmd = [gemini_path, "chat", "--model", model_name, full_prompt]
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, encoding='utf-8'
        )
        
        stdout_acc = ""
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None: break
            if line:
                print(line.strip())
                if log_file_handle:
                    log_file_handle.write(line)
                    log_file_handle.flush()
                stdout_acc += line
        
        parse_and_execute_side_effects(stdout_acc)

    finally:
        if log_file_handle: log_file_handle.close()

if __name__ == "__main__":
    main()
