# Skill: Synthetic Data & Scenario Generation

## Description
This skill focuses on generating synthetic test data and edge-case scenarios to ensure the robustness of "Vibe Coding" outputs.

## Usage
Use this skill when:
-   You have just written a feature (Vibe Coding "Run" phase).
-   You need to verify it but lack real data.
-   You want to prevent "Vibe Hallucinations" (code that looks good but fails on edge cases).

## Steps
1.  **Analyze**: Look at the code you just wrote.
2.  **Imagine**: "What is the worst input possible?" (Null, Huge String, Negative Numbers, Injection).
3.  **Generate**: Create a JSON/CSV payload or a Test Fixture representing these cases.
    -   *Do not* ask the user for data if you can synthesize it.
4.  **Verify**: Run the code against this synthetic data.

## Example
"Generate 50 borderline valid email addresses and 50 invalid ones to test the regex validator."
