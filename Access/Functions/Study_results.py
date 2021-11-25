#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None
    grades = 0
    sum = 0.0

    file1 = open(path, 'r')

    for line in file1.readlines():
        gr = line.find(':')
        if not gr == -1:
            grades += 1
            sum += float(line[gr + 1:])

    file1.close()

    if grades == 0:
        return 0.0
    else:
        return sum / grades


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("my_grades.txt"))
