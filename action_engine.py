# Action Engine
# Decides what actions should be taken based on rule_engine issues


def apply_rules(record):

    actions = []

    # Rename file if normalization rule triggered
    if "filename_not_normalized" in record["issues"]:
        actions.append(
            {
                "type": "rename",
                "new_name": record["normalized_name"],
                "reason": "filename normalization",
            }
        )

    # Archive outdated files
    if "outdated_file" in record["issues"]:
        actions.append(
            {"type": "archive", "destination": "archive", "reason": "outdated file"}
        )

    # Move compiled artifacts
    if "compiled_artifact" in record["issues"]:
        actions.append(
            {"type": "move", "destination": "build", "reason": "compiled artifact"}
        )

    # Move sensitive files
    if "sensitive_file" in record["issues"]:
        actions.append(
            {
                "type": "move",
                "destination": "sensitive",
                "reason": "potential secret file",
            }
        )

    # Organize files by category
    if record.get("category"):
        actions.append(
            {
                "type": "organize",
                "destination": record["category"],
                "reason": "file classification",
            }
        )

    record["actions"] = actions

    return record
