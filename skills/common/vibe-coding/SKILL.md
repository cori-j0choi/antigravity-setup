# Skill: Vibe Coding Workflow

## Description
"Vibe Coding" emphasizes strict adherence to "Think-Run-Feedback" loops, rapid iteration, and maintaining a clean context ("Context Hygiene") to maximize LLM performance.

## Core Principles

### 1. Think-Run-Feedback Loop
- **Think**: Before writing code, briefly plan the step in your head or scratchpad.
- **Run**: Write the minimal code to satisfy the current step.
- **Feedback**: IMMEDIATELY run the code/test. Do not write 10 files before running one.
- **Correction**: If it fails, fix it. If it works, commit/save and move to the next.

### 2. Context Hygiene
- **Reduce Noise**: Close irrelevant files before asking the LLM.
- **Specific Queries**: Don't ask "Fix this." Ask "Fix the `IndexError` in `utils.py` line 42."
- **Reset Often**: If the conversation gets too long or confused, summarize progress and start a fresh session (or clear context).

### 3. Micro-Commits
- Commit working states frequently. This acts as a save point for the LLM's memory.

## Trigger
- Use this skill when:
    - Debugging complex issues (requires tight feedback loops).
    - Developing new features from scratch (iterative build).
    - Working with large codebases (requires context hygiene).
