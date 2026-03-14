import datetime
from pathlib import Path

# original path
# new path
# rule triggered
# action taken
# timestamp
# success/failure reason

# create folder if it doesnt exist
original_dir = Path("original_dir").mkdir(exist_ok=True)
new_dir = Path("new_folder").mkdir(exist_ok=True)


rules = []
actions = []
is_file_success = True

dir_info = Path("new_folder").stat()


new_folder_timestamp = datetime.datetime.fromtimestamp(dir_info.st_ctime)

print(new_folder_timestamp)

if is_file_success:
    print("success")
    # TODO
else:
    print("failed")
    # TODO
