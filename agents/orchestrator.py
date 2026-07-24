from agents.triage_agent import classify_bug
from agents.log_analysis_agent import analyze_log
from utils.save_output import save_analysis


def run_agents(bug_description, stack_text):

    # Run Triage Agent
    triage_result = classify_bug(bug_description)

    # Run Log Analysis Agent
    log_result = analyze_log(stack_text)

    # Combine Results
    combined_result = {

        "bug_description": bug_description,

        "triage": {

            "severity": triage_result["severity"],

            "priority": triage_result["priority"],

            "component": triage_result["component"],

            "confidence": triage_result["confidence"],

            "reason": triage_result["reason"],

            "suggested_action": triage_result["suggested_action"]

        },

        "log_analysis": {

            "exception": log_result["exception"],

            "failure": log_result["failure"],

            "code_path": log_result["code_path"]

        }

    }

    save_analysis(combined_result)

    return {

        "severity": triage_result["severity"],

        "priority": triage_result["priority"],

        "component": triage_result["component"],

        "confidence": triage_result["confidence"],

        "reason": triage_result["reason"],

        "suggested_action": triage_result["suggested_action"],

        "exception": log_result["exception"],

        "failure": log_result["failure"],

        "code_path": log_result["code_path"]

    }