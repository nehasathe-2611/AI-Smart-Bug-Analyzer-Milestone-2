import random
import time

from agents.orchestrator import run_agents
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(

        "index.html",

        bug_description="",

        stack_filename="",

        error_filename="",

        severity="-",

        priority="-",

        severity_class="",

        priority_class="",

        component="-",

        confidence="-",
        confidence_value=0,

        analysis_time=0,

        reasoning="-",

        suggested_action="-",

        exception="-",

        failure="-",

        code_path="-"

    )


@app.route("/analyze", methods=["POST"])
def analyze():

    bug_description = request.form.get("bug_description")

    start_time = time.time()

    stack_trace = request.files.get("stack_trace")

    error_log = request.files.get("error_log")

    stack_text = ""

    if stack_trace and stack_trace.filename != "":

        stack_text = stack_trace.read().decode("utf-8", errors="ignore")

        stack_trace.seek(0)

    combined_result = run_agents(
        bug_description,
        stack_text
    )

    analysis_time = "{:.3f}".format(
        time.time() - start_time
    )

    bug_id = "BUG-" + str(random.randint(1000,9999))

    print("Bug Description:")
    print(bug_description)

    if stack_trace:
        print("Stack Trace :", stack_trace.filename)

    if error_log:
        print("Error Log :", error_log.filename)

    severity = combined_result["severity"]
    priority = combined_result["priority"]

    severity_class = severity.lower()
    priority_class = priority.lower()

    return render_template(
        "index.html",

        bug_id=bug_id,

        bug_description=bug_description,

        stack_filename=stack_trace.filename if stack_trace and stack_trace.filename else "",

        error_filename=error_log.filename if error_log and error_log.filename else "",

        severity=severity,
        priority=priority,

        severity_class=severity_class,
        priority_class=priority_class,

        component=combined_result["component"],

        confidence=combined_result["confidence"],

        confidence_value=int(
            combined_result["confidence"].replace("%", "")
        ),

        analysis_time=analysis_time,

        reasoning=combined_result["reason"],

        suggested_action=combined_result["suggested_action"],

        exception=combined_result["exception"],
        failure=combined_result["failure"],
        code_path=combined_result["code_path"]
    )


if __name__ == "__main__":
    app.run(debug=True)