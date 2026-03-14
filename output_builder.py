import shutil
from pathlib import Path


def build_output(record, base_dir="clean"):

    source_path = Path(record["path"])

    # Decide destination folder
    destination_folder = record.get("category", "misc")

    # Archive outdated files
    if "outdated_file" in record["issues"]:
        destination_folder = "archive"

    # Use normalized filename if it exists
    new_name = record.get("normalized_name", record["name"])

    # Build destination path
    destination_dir = Path(base_dir) / destination_folder
    destination_dir.mkdir(parents=True, exist_ok=True)

    destination_path = destination_dir / new_name

    # Copy file
    shutil.copy2(source_path, destination_path)

    print(f"{source_path.name} → {destination_path}")

    return str(destination_path)
