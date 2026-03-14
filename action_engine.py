# Applies safe corrections such as:

# rename file

# move file to a better folder

# tag/archive outdated files

# normalize metadata

# Risky actions should be optional or require approval
#
def apply_rule(file, rules):

    corrections = rules
    is_risky = False
    for correction in corrections:
        if file == correction:
            # TODO
            print("apply correction")
            if is_risky:
                # TODO
                print("needs approval")
