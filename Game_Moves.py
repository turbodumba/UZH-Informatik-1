#!/usr/bin/env python3
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):
    # 1. Test if the playing field is valid
    all_dir = ["down", "left", "right", "up"]
    if not direction in all_dir:
        raise Warning("Direction parameter invalid")
    player = 0
    index_player_one = 0
    index_player_two = 0
    if not len(state) > 0:
        raise Warning("0 Rows")
    else:
        len_of_all = len(state[0])
        index_one = 0
        for line in state:
            if not len(line) == len_of_all or len(line) == 0:
                raise Warning("Wrong length or 0 Columns")
            index_two = 0
            for sign in line:
                if not (sign == " " or sign == "#" or sign == "o"):
                    raise Warning("Invalid Character in the map")
                elif sign == "o":
                    player += 1
                    index_player_one = index_one
                    index_player_two = index_two
                index_two += 1
            index_one += 1
    if not 0 < player < 2:
        raise Warning("Zero or too many players")

    # 2. Test if moves are possible
    def find_possible_dir(fstate, findex_player_one, findex_player_two, flen_of_all):
        height = len(fstate)
        up = False
        down = False
        left = False
        right = False

        if findex_player_two + 1 < flen_of_all:
            if fstate[findex_player_one][findex_player_two + 1] == " ":
                right = True
        if not findex_player_two == 0:  # first column
            if fstate[findex_player_one][findex_player_two - 1] == " ":
                left = True
        if findex_player_one + 1 < height:
            if fstate[findex_player_one + 1][findex_player_two] == " ":
                down = True
        if not findex_player_one == 0:  # first row
            if fstate[findex_player_one - 1][findex_player_two] == " ":
                up = True
        return [down, left, right, up]

    possible_dir = find_possible_dir(state, index_player_one, index_player_two, len_of_all)

    if not any(possible_dir):
        raise Warning("No direction is possible")
    if direction == "down":
        if not possible_dir[0]:
            raise Warning("Direction down not possible")
    elif direction == "left":
        if not possible_dir[1]:
            raise Warning("Direction left not possible")
    elif direction == "right":
        if not possible_dir[2]:
            raise Warning("Direction right not possible")
    elif direction == "up":
        if not possible_dir[3]:
            raise Warning("Direction up not possible")

    # 3. Generate new field after doing move
    newstate_list = []
    if direction == "up":
        index_one = 0
        for line in state:
            if index_one == index_player_one - 1:
                string = line[:index_player_two] + "o" + line[index_player_two + 1:]
                newstate_list.append(string)
                new_player_one = index_one
                new_player_two = index_player_two
            elif index_one == index_player_one:
                string = line[:index_player_two] + " " + line[index_player_two + 1:]
                newstate_list.append(string)
            else:
                newstate_list.append(line)
            index_one += 1
    elif direction == "down":
        index_one = 0
        for line in state:
            if index_one == index_player_one + 1:
                string = line[:index_player_two] + "o" + line[index_player_two + 1:]
                newstate_list.append(string)
                new_player_one = index_one
                new_player_two = index_player_two
            elif index_one == index_player_one:
                string = line[:index_player_two] + " " + line[index_player_two + 1:]
                newstate_list.append(string)
            else:
                newstate_list.append(line)
            index_one += 1
    else:
        index_one = 0
        for line in state:
            if index_one == index_player_one:
                if direction == "left":
                    string = line[:index_player_two - 1] + "o" + " " + line[index_player_two + 1:]
                    newstate_list.append(string)
                    new_player_one = index_one
                    new_player_two = index_player_two - 1
                elif direction == "right":
                    string = line[:index_player_two] + " " + "o" + line[index_player_two + 2:]
                    newstate_list.append(string)
                    new_player_one = index_one
                    new_player_two = index_player_two + 1
            else:
                newstate_list.append(line)
            index_one += 1

    # 4. Find possible moves
    newstate = tuple(newstate_list)
    new_poss_dir = find_possible_dir(newstate, new_player_one, new_player_two, len_of_all)
    dir_list = []
    if new_poss_dir[0]:
        dir_list.append("down")
    if new_poss_dir[1]:
        dir_list.append("left")
    if new_poss_dir[2]:
        dir_list.append("right")
    if new_poss_dir[3]:
        dir_list.append("up")
    ret_tup = (newstate, tuple(dir_list))
    return ret_tup

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
