# Applies safe corrections such as:

# rename file

# move file to a better folder

# tag/archive outdated files

# normalize metadata

# Risky actions should be optional or require approval
file = "file"
corrections = ["rename file", "move file", "tag", "normalize"]
is_risky = False
for correction in corrections:
    if file == correction:
        # TODO
        print("apply correction")
        if is_risky:
            # TODO
            print("needs approval")
