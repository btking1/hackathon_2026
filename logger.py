import datetime
from pathlib import Path

# Log file location
LOG_FILE = Path("change_log.txt")


def log_change(original_path, new_path, issues, actions, success, reason=""):
    """
    Write a log entry describing the change made to a file.
    """

    timestamp = datetime.datetime.now()

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"Timestamp: {timestamp}\n")
        log.write(f"Original Path: {original_path}\n")
        log.write(f"New Path: {new_path}\n")
        log.write(f"Issues Detected: {issues}\n")
        log.write(f"Actions Taken: {actions}\n")
        log.write(f"Success: {success}\n")

        if reason:
            log.write(f"Reason: {reason}\n")

        log.write("-" * 50 + "\n")
