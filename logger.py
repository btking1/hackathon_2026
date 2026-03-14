import datetime
from pathlib import Path

# original path
# new path
# rule triggered
# action taken
# timestamp
# success/failure reason

original_dir = Path("/original_dir").mkdir(exist_ok=True)
new_dir = Path("/new_folder").mkdir(exist_ok=True)

rules = []
actions = []
