#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    mergelist = []
    if a == [] or b == []:
        return mergelist

    if len(a) > len(b):
        for index in range(len(a)):
            if index < (len(b) - 1):
                mergelist.append((a[index], b[index]))
            else:
                mergelist.append((a[index],b[-1]))
    else:
        for index in range(len(b)):
            if index < (len(a) - 1):
                mergelist.append((a[index], b[index]))
            else:
                mergelist.append((a[-1], b[index]))

    return mergelist


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))  # should return[(0, 5), (1, 6), (2, 6)]
print(merge([0, 1, 2], [5, 6, 7]))  # should return [(0, 5), (1, 6), (2, 7)]
print(merge([2, 1, 0], [5, 6]))  # should return [(2, 5), (1, 6), (0, 6)]
print(merge([], [2, 3]))  # should return []
