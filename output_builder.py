# import os
import shutil
from pathlib import Path

Path("new_folder").mkdir(exist_ok=True)

directory = Path(
    "/Users/godsiom/Library/Mobile Documents/com~apple~CloudDocs/NCAT/Spring 2026/ECEN 356"
)

for file in directory.rglob("*"):
    shutil.copy(file, "new_folder/")
    print(f"file {file} successfully moved")
