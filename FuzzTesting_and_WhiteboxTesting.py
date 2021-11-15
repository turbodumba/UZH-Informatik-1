# !/usr/bin/env python3
import random

# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_length_global = 1
max_length_global = 5
char_start_global = 30
char_end_global = 65


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fuzzer(min_length, max_length, char_start, char_end):
    rand_string = ""
    random_range = random.randint(min_length, max_length)
    for i in range(0, random_range):
        random_num = random.randint(char_start, char_end)
        rand_string += chr(random_num)
    return rand_string


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def calculate_factorial(inp):
    # 1. Test if possible
    if inp is None:
        return None
    if isinstance(inp, str):
        try:
            number = int(inp)
        except:
            raise TypeError("TypeError: string")
    else:
        number = inp

    if number < 0:
        raise ValueError("ValueError: number negative")
    if number > 10:
        raise ValueError("ValueError: number too large")
    # 2. Calculate Factorial
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def run(trials):
    # this function should make use of the other two functions
    # for the input of the fuzzer functions use the global variables
    # this is required else the automatic testing is not working
    ret_list = []
    for i in range(0, trials):
        cal_inp = fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
        try:
            calculate_factorial(cal_inp)
            ret_tup = (0, "")
        except ValueError as e:
            ret_tup = (1, str(e))
        except:
            ret_tup = (1, "Other error")
        ret_list.append(ret_tup)
    return ret_list


# The following line calls the function run and prints the return
# value to the Console.



print(run(10))
