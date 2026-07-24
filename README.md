# 🐞 AI Smart Bug Analyzer

> An AI-powered Multi-Agent Bug Analysis System built using **Python**, **Flask**, and **Rule-Based AI** to automate software bug triage and log analysis.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Project](https://img.shields.io/badge/Infosys-Springboard-orange)

---

# 📌 Project Overview

AI Smart Bug Analyzer is a Flask-based web application developed as part of the **Infosys Springboard Virtual Internship (Milestone 2)**.

The application uses a **Multi-Agent Architecture** to analyze software bug reports automatically.

It accepts a bug description and optional stack trace or error log, then performs:

- Bug Triage
- Log Analysis
- Severity Prediction
- Priority Prediction
- Component Detection
- Exception Detection
- Suggested Action Generation

The goal is to help developers identify and prioritize software bugs more efficiently.

---

# 🚀 Features

### 🤖 Triage Agent

- Predicts Bug Severity
- Predicts Bug Priority
- Detects Affected Component
- Calculates Confidence Score
- Provides Reasoning
- Generates Suggested Action

---

### 📄 Log Analysis Agent

- Detects Exception Type
- Extracts Failure Point
- Detects Affected Code Path
- Supports Python and Java Stack Traces

---

### ⚙️ Additional Features

- Auto-generated Bug ID
- Analysis Time Calculation
- Rule-Based Decision Engine
- Responsive Flask Dashboard
- File Upload Support
- Clean User Interface

---

# 🏗️ Project Architecture

```text
                User

                  │

                  ▼

        Flask Web Application

                  │

                  ▼

            Orchestrator

        ┌─────────┴─────────┐

        ▼                   ▼

 Triage Agent       Log Analysis Agent

        │                   │

        └─────────┬─────────┘

                  ▼

          Combined Analysis

                  ▼

        Analysis Dashboard
```

---

# 📂 Project Structure

```text
AI-Smart-Bug-Analyzer/

│

├── agents/
│   ├── triage_agent.py
│   ├── log_analysis_agent.py
│   └── orchestrator.py
│
├── sample_data/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── utils/
│   └── save_output.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Rule-Based Artificial Intelligence
- Regular Expressions (Regex)

---

# 🔄 Workflow

1. User submits a bug description.
2. User optionally uploads a stack trace or error log.
3. Triage Agent analyzes the bug report.
4. Log Analysis Agent extracts exception details.
5. Orchestrator combines outputs from both agents.
6. Final analysis is displayed on the dashboard.

---

# 📊 Output Generated

The application generates:

- 🆔 Bug ID
- 🚨 Severity
- ⚡ Priority
- 📦 Affected Component
- 📈 Confidence Score
- ⏱️ Analysis Time
- 💡 Triage Reasoning
- 🛠️ Suggested Action
- ❗ Exception Type
- 📍 Failure Point
- 📄 Affected Code Path

---

# 🧪 Sample Test Cases

| Bug Description | Expected Severity |
|----------------|-------------------|
| Application crashes after login | Critical |
| Database timeout | High |
| Application is slow | Medium |
| Button alignment incorrect | Low |

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/nehasathe-2611/AI-Smart-Bug-Analyzer-Milestone-2.git
```

Go to the project directory

```bash
cd AI-Smart-Bug-Analyzer-Milestone-2
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```text
http://127.0.0.1:5000
```

---

# 🎯 Internship Deliverables Covered

✅ Bug Submission Module

✅ Triage Agent

✅ Log Analysis Agent

✅ Multi-Agent Orchestration

✅ Structured Output Generation

✅ Validation using Sample Bug Reports

---

# 🔮 Future Enhancements

- Machine Learning based Bug Classification
- LLM Integration
- Duplicate Bug Detection
- Root Cause Analysis Agent
- Bug History Database
- Dashboard Analytics
- PDF Report Generation
- User Authentication

---

# 👩‍💻 Author

**Neha Sathe**

MCA Student | AI/ML Research Intern

📍 Solapur, Maharashtra, India

---

# 📜 Acknowledgement

This project was developed as part of the **Infosys Springboard Virtual Internship** to demonstrate a **Multi-Agent AI workflow** for automated software bug analysis, bug triage, and log analysis.

---
⭐ If you found this project useful, consider giving it a Star on GitHub.