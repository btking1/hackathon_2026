# Rule Engine

# Evaluates each file against hygiene policies

# Example rules:

# invalid or inconsistent file names

# missing metadata

# misplaced files

# stale or outdated files

# duplicate or near-duplicate files

# irrelevant files for the directory category
rules = [
    "invalid or inconsistent file names",
    "missing metadata",
    "misplaced files",
    "stale or outdated files",
    "duplicate or near-duplicate files",
    "irrelevant files for the directory category",
]
files = []

# evaluate
for file in files:
    for rule in rules:
        if file == rule:
            print("apply rule")
