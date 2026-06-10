def analyze_logs():
    sample_logs = [
        "INFO: Service started",
        "WARNING: Memory usage high",
        "ERROR: Database connection failed",
        "INFO: User login successful"
    ]

    errors = []

    for log in sample_logs:
        if "ERROR" in log:
            errors.append(log)

    return errors