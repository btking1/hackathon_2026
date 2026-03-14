import re


def evaluate_rules(record):

    name = record["name"].lower()

    if " " in name:
        record["issues"].append("spaces_in_filename")

    if name.endswith(".pyc"):
        record["issues"].append("compiled_artifact")

    if "secret" in name:
        record["issues"].append("sensitive_file")

    return record


def normalize_filename(record):

    name = record["name"]

    cleaned = name.lower()
    cleaned = cleaned.replace(" ", "_")
    cleaned = re.sub(r"[()]", "", cleaned)
    cleaned = re.sub(r"__+", "_", cleaned)

    if cleaned != name:
        record["issues"].append("filename_not_normalized")

    record["normalized_name"] = cleaned

    return record


def classify_file(record):

    ext = record["extension"].lower()

    if ext in [".py", ".cpp"]:
        record["category"] = "code"

    elif ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".heic"]:
        record["category"] = "images"

    elif ext in [".csv", ".xlsx"]:
        record["category"] = "finance"

    elif ext in [".pdf"]:
        record["category"] = "research"

    elif ext in [".docx", ".pptx"]:
        record["category"] = "docs"

    elif ext in [".log"]:
        record["category"] = "logs"

    else:
        record["category"] = "misc"

    return record


def detect_outdated(record):

    name = record["name"].lower()

    keywords = ["old", "superseded", "copy of"]

    for word in keywords:
        if word in name:
            record["issues"].append("outdated_file")
            break

    return record


# Rule registry
RULES = [evaluate_rules, normalize_filename, classify_file, detect_outdated]
