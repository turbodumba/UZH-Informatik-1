#!/usr/bin/env python3
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):
    # 1. Test if move is possible and the playing field is valid
    player = 0
    if not len(state) > 0:
        raise Warning("Bruh")
    else:
        len_of_all = len(state[0])
        for line in state:
            if not len(line) == len_of_all or len(line) == 0:
                raise Warning
            for sign in line:
                if not sign == " " or not sign == "#" or not sign == "o":
                    raise Warning
                elif sign == "o":
                    player += 1


    # 2. Generate new field after doing move
    # 3. Find possible moves


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
)
s2 = move(s1, "right")

print("= New State =")
print("\n".join(s2[0]))
print("\nPossible Moves: {}".format(s2[1]))
