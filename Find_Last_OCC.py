def find_last(string, char):
    same = False
    if string is None:
        return -1
    if string == "":
        return -1

    if string[-1] == char:
        same = True
    tup = find_last(string[:len(string)-1], char)
    if same:
        tup_new = len(string)-1
        return tup_new
    else:
        return tup









# returns 0
#print(find_last("The quick brown fox jumps over the lazy dog", "T"))
# returns 42
print(find_last("The quick brown fox jumps over the lazy dog", "g"))
# returns 4
print(find_last("The quick brown fox jumps over the lazy dog", "q"))
# returns -1
print(find_last("The quick brown fox jumps over the lazy dog", "X"))
# returns -1
print(find_last("The quick brown fox jumps over the lazy dog", "u"))
print(find_last("The quick brown fox jumps over the lazy dog", "o"))
print(find_last("", "a"))
# returns -1
print(find_last(None, "a"))