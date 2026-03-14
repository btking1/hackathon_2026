import datetime

# import os
from pathlib import Path


def get_folder():
    file = input("Enter file name: ")
    # print(file)
    return file


directory = Path(get_folder())

print(directory)

records = []

for file in directory.rglob("*"):
    if file.is_file():
        stats = file.stat()

        info = {
            "path": str(file),
            "name": file.name,
            "extension": file.suffix,
            "size_bytes": stats.st_size,
            "created": datetime.datetime.fromtimestamp(stats.st_ctime),
            "modified": datetime.datetime.fromtimestamp(stats.st_mtime),
            "accessed": datetime.datetime.fromtimestamp(stats.st_atime),
        }
        print(info)

        records.append(info)

print(records)
