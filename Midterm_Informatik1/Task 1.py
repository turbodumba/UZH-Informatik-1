def greetings(names):
    zero = True
    ret_string = "Hello"
    l = len(names)
    ind = 0
    for name in names:
        zero = False
        if l == 1:
            ret_string += " " + name
        elif ind == l - 1 and not l == 0:
            ret_string += " and " + name
        elif ind == l - 2:
            ret_string += " " + name
        else:
            ret_string += " " + name + ","
        ind += 1
    if zero:
        return ret_string + "?"
    else:
        return ret_string + "."


assert (greetings([]) == 'Hello?')
assert (greetings(['Josh']) == 'Hello Josh.')
assert (greetings(['Josh', 'Alice']) == 'Hello Josh and Alice.')
assert (greetings(['Josh', 'Alice', 'Marie']) == 'Hello Josh, Alice and Marie.')
