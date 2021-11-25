#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def is_prime(n):
    s = f'{n} is prime'
    if n == 1:
        ret = "1 is the multiplicative identity"
        return ret

    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            b = int(n / a)
            s = f'{n} is not a prime number ({a} * {b} = {n})'
            return s

    return s


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(is_prime(1))
