import datetime
from pathlib import Path


def scan_folder():
    folder_name = input("Enter folder path: ")
    directory = Path(folder_name)

    if not directory.exists() or not directory.is_dir():
        print("Invalid directory.")
        return None

    records = []

    for item in directory.rglob("*"):
        if item.is_file():
            stats = item.stat()

            info = {
                "path": str(item),
                "name": item.name,
                "extension": item.suffix.lower(),
                "size_bytes": stats.st_size,
                "created": datetime.datetime.fromtimestamp(stats.st_ctime),
                "modified": datetime.datetime.fromtimestamp(stats.st_mtime),
                "accessed": datetime.datetime.fromtimestamp(stats.st_atime),
                "issues": [],
                "actions": [],
                "category": None,
            }

            records.append(info)

    return records
