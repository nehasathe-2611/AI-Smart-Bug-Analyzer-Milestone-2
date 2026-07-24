import os
import sys

# Allow importing from project folders
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from agents.orchestrator import run_agents


sample_folder = "sample_data"

files = sorted(os.listdir(sample_folder))

print("=" * 70)
print("AI SMART BUG ANALYZER - VALIDATION REPORT")
print("=" * 70)

for file in files:

    # Ignore non-txt files
    if not file.endswith(".txt"):
        continue

    file_path = os.path.join(sample_folder, file)

    with open(file_path, "r", encoding="utf-8") as f:
        bug_text = f.read()

    result = run_agents(
        bug_description=bug_text,
        stack_text=bug_text
    )

    print("\n")
    print("=" * 70)
    print("File :", file)
    print("=" * 70)

    print("Severity :", result["severity"])
    print("Priority :", result["priority"])
    print("Component :", result["component"])

    print("Confidence :", result["confidence"])

    print("Reason :", result["reason"])

    print("Exception :", result["exception"])

    print("Failure Point :", result["failure"])

    print("Code Path :", result["code_path"])

print("\n")
print("=" * 70)
print("Validation Completed Successfully")
print("=" * 70)