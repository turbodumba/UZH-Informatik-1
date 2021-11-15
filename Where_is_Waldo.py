def where_is_waldo(names):
    index = 0
    returnind = -1
    for name in names:
        if name == "Waldo":
            returnind = index
            break
        index += 1

    if returnind == -1:
        return None
    else:
        return returnind


assert (where_is_waldo(["Peter", "Waldo", "John"]) == 1)
assert (where_is_waldo(["Peter", "Willy", "John"]) == None)
assert (where_is_waldo([]) == None)
