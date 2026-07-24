def classify_bug(description):

    description = description.lower()
    match_score = 0

    severity = "Low"
    priority = "Low"
    component = "General"
    confidence = "70%"
    reason = "No critical keywords found."
    suggested_action = "Review the issue and reproduce the bug before fixing."

    # Critical bugs
    if any(word in description for word in
    [
        "crash",
        "fatal",
        "panic",
        "shutdown",
        "system down"
    ]):

        severity = "Critical"
        priority = "Critical"
        match_score += 4
        reason = "Critical system failure detected."
        suggested_action = "Immediately investigate system logs and restore the affected service."


    # High severity
    elif any(word in description for word in
    [
        "exception",
        "error",
        "failed",
        "failure",
        "timeout",
        "unable",
        "not responding",
        "freeze"
    ]):

        severity = "High"
        priority = "High"
        match_score += 3
        reason = "High severity software issue detected."
        suggested_action = "Assign to the development team and fix before the next release."


    # Medium severity
    elif any(word in description for word in
    [
        "slow",
        "delay",
        "warning",
        "performance",
        "retry"
    ]):

        severity = "Medium"
        priority = "Medium"
        match_score += 2
        reason = "Performance related issue detected."
        suggested_action = "Optimize the affected module and monitor application performance."


    # Low severity
    elif any(word in description for word in
    [
        "typo",
        "alignment",
        "color",
        "spacing",
        "font"
    ]):

        severity = "Low"
        priority = "Low"
        match_score += 1
        reason = "Minor user interface issue detected."
        suggested_action = "Schedule the issue for the next UI improvement cycle."

    # Authentication
    if any(word in description for word in
    [
        "login",
        "authentication",
        "password",
        "signin",
        "signup",
        "otp",
        "user account"
    ]):
        component = "Authentication"
        match_score += 1


    # Database
    elif any(word in description for word in
    [
        "database",
        "mysql",
        "sql",
        "query",
        "mongodb",
        "postgres"
    ]):
        component = "Database"
        match_score += 1


    # Frontend
    elif any(word in description for word in
    [
        "ui",
        "button",
        "screen",
        "page",
        "layout",
        "alignment",
        "font",
        "color"
    ]):
        component = "Frontend"
        match_score += 1


    # API
    elif any(word in description for word in
    [
        "api",
        "endpoint",
        "request",
        "response",
        "rest"
    ]):
        component = "API"
        match_score += 1


    # Upload
    elif any(word in description for word in
    [
        "upload",
        "file",
        "image",
        "attachment"
    ]):
        component = "File Upload"
        match_score += 1


    # Payment
    elif any(word in description for word in
    [
        "payment",
        "upi",
        "transaction",
        "invoice",
        "billing"
    ]):
        component = "Payment"
        match_score += 1


    # Network
    elif any(word in description for word in
    [
        "network",
        "internet",
        "connection",
        "offline",
        "server"
    ]):
        component = "Network"
        match_score += 1


    # Security
    elif any(word in description for word in
    [
        "security",
        "permission",
        "access denied",
        "unauthorized"
    ]):
        component = "Security"
        match_score += 1

    # Calculate confidence based on match_score
    if match_score >= 5:
        confidence = "98%"
    elif match_score == 4:
        confidence = "94%"
    elif match_score == 3:
        confidence = "90%"
    elif match_score == 2:
        confidence = "82%"
    else:
        confidence = "72%"

    return {
        "severity": severity,
        "priority": priority,
        "component": component,
        "confidence": confidence,
        "reason": reason,
        "suggested_action": suggested_action
    }