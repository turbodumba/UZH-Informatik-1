#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def read_csv(path):
    file = open(path, 'r')
    tuplelist = []
    for line in file.readlines():
        if line == "\n":
            continue
        else:
            liste = []
            for word in line.split(','):
                if word.find('\n') == -1:
                    liste.append(str(word))
                else:
                    here = word.find('\n')
                    liste.append(str(word[:here]))
            tup = tuple(liste)
            tuplelist.append(tup)
    file.close()
    return tuplelist
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(read_csv("../titanic.csv"))
