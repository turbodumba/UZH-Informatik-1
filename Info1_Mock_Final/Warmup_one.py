def find_both_ways(text, word):
    textlow = text.lower()
    if word.lower() in textlow:
        return (True, 1)
    elif word.lower() in textlow[::-1]:
        return (True, -1)
    else:
        return (False, 0)

    # DO NOT SUBMIT THE LINES BELOW!


assert (find_both_ways("Hello, World!", "lo, wo") == (True, 1))
assert (find_both_ways("Hello, God!", "Dog") == (True, -1))
assert (find_both_ways("Hello, California!", "local") == (False, 0))
