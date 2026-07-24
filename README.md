# AI Smart Bug Analyzer

## Overview

AI Smart Bug Analyzer is a Flask-based multi-agent application that
analyzes software bug reports using a rule-based approach. The system
classifies bug severity, priority, and affected component, extracts
useful information from uploaded stack traces, and provides a suggested
action for developers.

## Features

-   Bug report submission
-   Stack trace upload (.txt)
-   Error log upload (.txt)
-   Rule-based Triage Agent
    -   Severity classification
    -   Priority assignment
    -   Component identification
    -   Confidence score
    -   Reasoning
    -   Suggested action
-   Log Analysis Agent
    -   Exception detection
    -   Failure point extraction
    -   Affected code path detection
-   Analysis time measurement
-   Auto-generated Bug ID
-   Responsive dashboard UI

## Project Structure

``` text
AI-Smart-Bug-Analyzer/
├── agents/
│   ├── triage_agent.py
│   ├── log_analysis_agent.py
│   └── orchestrator.py
├── sample_data/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── utils/
│   └── save_output.py
├── app.py
├── requirements.txt
└── README.md
```

## Technologies Used

-   Python
-   Flask
-   HTML5
-   CSS3
-   Rule-Based AI
-   Regular Expressions (Regex)

## Workflow

1.  User submits a bug description.
2.  Optional stack trace and error log are uploaded.
3.  Triage Agent classifies the bug.
4.  Log Analysis Agent extracts exception details.
5.  Orchestrator combines results.
6.  Dashboard displays the final analysis.

## Installation

``` bash
git clone <repository-url>
cd AI-Smart-Bug-Analyzer
python -m venv venv
```

Activate the environment.

Windows:

``` bash
venv\Scripts\activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run:

``` bash
python app.py
```

Open: http://127.0.0.1:5000

## Example Test Cases

  Bug Description                   Expected Severity
  --------------------------------- -------------------
  Application crashes after login   Critical
  Database timeout                  High
  Application is slow               Medium
  Button alignment incorrect        Low

## Future Enhancements

-   ML-based bug classification
-   LLM integration
-   PDF report export
-   Bug history
-   Dashboard analytics
-   User authentication

## Author

**Neha Sathe**

MCA Student \| AI/ML Research Intern

Developed as part of the Infosys Springboard Virtual Internship.
