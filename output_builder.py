# import os
import shutil
from pathlib import Path


# build output folder using file name and the file type/category
def output_builder(file, type):

    # create new folder
    Path(type).mkdir(exist_ok=False)

    file = Path(file)
    new_directory = Path(f"clean/{type}")

    # copy file into new directory
    shutil.copy(file, new_directory)
    print(f"file {file} to {new_directory} successfully moved")
