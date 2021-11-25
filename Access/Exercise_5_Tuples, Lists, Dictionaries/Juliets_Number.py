#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ['0779266313', '0789266313', '0792566313', '0792646313', '0792663113', '0792663130', '0792663213', '0792663313', '0792696313', '0796266313']


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    all_pos = []
    for i in range(2, 10):
        for j in range(10):
            num = n[:i] + str(j) + n[i:]
            for k in wa_nrs:
                if num == k:
                    if not num in all_pos:
                        all_pos.append(num)
    return all_pos

    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet

    # Don't forget to return your result


# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("079266313"))
