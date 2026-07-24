import re


def analyze_log(log_text):

    exception = "Unknown Exception"
    failure = "Unknown"
    code_path = "Unknown"

    # Detect common exceptions

    exceptions = [

        # Python
        "TypeError",
        "ValueError",
        "IndexError",
        "KeyError",
        "AttributeError",
        "ModuleNotFoundError",
        "FileNotFoundError",
        "ImportError",
        "NameError",
        "ZeroDivisionError",
        "PermissionError",
        "RuntimeError",
        "MemoryError",

        # Java
        "NullPointerException",
        "ArrayIndexOutOfBoundsException",
        "ArithmeticException",
        "SQLException",
        "IOException",

        # JavaScript
        "ReferenceError",
        "SyntaxError",

        # Generic
        "Exception"

    ]

    for e in exceptions:
        if e in log_text:
            exception = e
            break

    # -----------------------------
    # Python Format
    # File "app.py", line 42
    # -----------------------------

    match = re.search(
        r'File "(.*?)", line (\d+)',
        log_text
    )

    if match:

        code_path = match.group(1)
        failure = "Line " + match.group(2)

    else:

        # -----------------------------
        # Java Format
        # Login.java:55
        # -----------------------------

        match = re.search(
            r'([A-Za-z0-9_]+\.(?:java|py|js|cs)):(\d+)',
            log_text
        )

        if match:

            code_path = match.group(1)
            failure = "Line " + match.group(2)

    if match:
        code_path = match.group(1)
        failure = "Line " + match.group(2)

    return {
        "exception": exception,
        "failure": failure,
        "code_path": code_path
    }