#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False
    f_in = open(path_reading, 'r')
    f_out = open(path_writing, 'w')
    title = False

    for line in f_in.readlines():
        if title:
            f_out.write("\n")
            title = False
        if line.find("Name") != -1:
            f_out.write("Firstname,Lastname")
            title = True
        elif line == "\n":
            f_out.write(",\n")
        elif line.find(";") != -1:
            space = line.find(";")
            n = line.find("\n")
            if n == -1:
                f_out.write(line[space + 2:] + "," + line[:space])
            else:
                f_out.write(line[space + 2:n] + "," + line[:space] + "\n")
        elif line.find(" ") != -1:
            space = line.find(" ")
            f_out.write(line[:space] + "," + line[space + 1:])

    f_in.close()
    f_out.close()


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(process_data("my_data.txt", "my_data_processed.txt"))
