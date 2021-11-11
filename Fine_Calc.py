#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fine_calculator(area, speed):
    if not isinstance(area, str):
        return "Invalid Area Type"
    if not isinstance(speed, int) and not isinstance(speed, float):
        return "Invalid Speed Type"
    if speed < 0:
        return "Invalid Speed Value"

    if area == "motorway":
        if (speed - 120) < 0:
            return 0
        else:
            percentage = (speed - 120) / 1.2
            return round(0.5 * (percentage ** 2))
    elif area == "expressway":
        if (speed - 100) < 0:
            return 0
        else:
            percentage = (speed - 100)
            return round(0.8 * (percentage ** 2))
    elif area == "urban":
        if (speed - 50) < 0:
            return 0
        else:
            percentage = (speed - 50) * 2
            return round(percentage**2)
    else:
        return "Invalid Area Value"

print(fine_calculator("motorway", 151))