#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gender_class_rates(dataset):
    # implement this function
    # the function might have other useful parameters, explore `help(round)`
    start_list = dataset[1]
    fc_male = 0
    fc_female = 0
    sc_male = 0
    sc_female = 0
    tc_male = 0
    tc_female = 0
    allpass = 0
    for tup in start_list:
        if (tup[3] == "male"):
            if tup[1] == 1:
                fc_male += 1
            elif tup[1] == 2:
                sc_male += 1
            elif tup[1] == 3:
                tc_male += 1
        elif (tup[3] == "female"):
            if tup[1] == 1:
                fc_female += 1
            elif tup[1] == 2:
                sc_female += 1
            elif tup[1] == 3:
                tc_female += 1
        allpass += 1


    perc_fcm = round(float(fc_male) / allpass *100, 1)
    if perc_fcm == 0:
        perc_fcm = None
    perc_scm = round(float(sc_male) / allpass * 100, 1)
    if perc_scm == 0:
        perc_scm = None
    perc_tcm = round(float(tc_male) / allpass * 100, 1)
    if perc_tcm == 0:
        perc_tcm = None
    perc_fcf = round(float(fc_female) / allpass * 100, 1)
    if perc_fcf == 0:
        perc_fcf = None
    perc_scf = round(float(sc_female) / allpass * 100, 1)
    if perc_scf == 0:
        perc_scf = None
    perc_tcf = round(float(tc_female) / allpass * 100, 1)
    if perc_tcf == 0:
        perc_tcf = None

    end_tuple = ((perc_fcm, perc_scm, perc_tcm), (perc_fcf, perc_scf, perc_tcf))
    return end_tuple


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!


# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the functions that you have written in Task 1+2.
# The following example is not complete.
print(gender_class_rates((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
        # ...
    ]
)))
