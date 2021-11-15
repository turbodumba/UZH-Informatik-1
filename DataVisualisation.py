#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def visualize(records):
    startlist = records[1]
    fc_pass = 0.0
    sc_pass = 0.0
    tc_pass = 0.0
    fc_surv = 0.0
    sc_surv = 0.0
    tc_surv = 0.0
    total_pass = 0.0

    for tup in startlist:
        if tup[1] == 1:
            fc_pass += 1
            if tup[0]:
                fc_surv += 1
        elif tup[1] == 2:
            sc_pass += 1
            if tup[0]:
                sc_surv += 1
        elif tup[1] == 3:
            tc_pass += 1
            if tup[0]:
                tc_surv += 1
        total_pass += 1

    stars = round(fc_pass / total_pass * 100 / 5)
    perc = round(fc_pass / total_pass * 100, 1)
    part_one = "Total |" + stars * "*" + (20 - stars) * " " + "| " + str(perc) + "%\n"
    stars = round(fc_surv / fc_pass * 100 / 5)
    perc = round(fc_surv / fc_pass * 100, 1)
    part_two = "Alive |" + stars * "*" + (20 - stars) * " " + "| " + str(perc) + "%\n"
    stars = round(sc_pass / total_pass * 100 / 5)
    perc = round(sc_pass / total_pass * 100, 1)
    part_three = "Total |" + stars * "*" + (20 - stars) * " " + "| " + str(perc) + "%\n"
    stars = round(sc_surv / sc_pass * 100 / 5)
    perc = round(sc_surv / sc_pass * 100, 1)
    part_four = "Alive |" + stars * "*" + (20 - stars) * " " + "| " + str(perc) + "%\n"
    stars = round(tc_pass / total_pass * 100 / 5)
    perc = round(tc_pass / total_pass * 100, 1)
    part_five = "Total |" + stars * "*" + (20 - stars) * " " + "| " + str(perc) + "%\n"
    stars = round(tc_surv / tc_pass * 100 / 5)
    perc = round(tc_surv / tc_pass * 100, 1)
    part_six = "Alive |" + stars * "*" + (20 - stars) * " " + "| " + str(perc) + "%"

    return_string = "== 1st Class ==\n" + part_one + part_two + "== 2nd Class ==\n" + part_three + part_four + \
                    "== 3rd Class ==\n" + part_five + part_six
    return return_string

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(visualize((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
    ]
)))

# == 1st Class ==
# Total |**                  | 10.1%
# Alive |*****               | 25.7%
# == 2nd Class ==
# Total |*******             | 32.7%
# Alive |*****               | 24.1%
# == 3rd Class ==
# Total |***********         | 57.2%
# Alive |****                | 19.8%
