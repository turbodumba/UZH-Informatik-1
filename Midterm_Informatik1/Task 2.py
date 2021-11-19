def no_unlucky(values, unlucky):
    if unlucky == 0:
        ret_val = 0
        for num in values:
            ret_val += num
        return ret_val
    else:
        summ = 0
        for num in values:
            if not num%unlucky==0:
                summ += num
        return summ


assert(no_unlucky([10, 24, 1], 13) == 35)
assert(no_unlucky([13, 25], 13) == 25)
assert(no_unlucky([13, 26], 13) == 0)
assert(no_unlucky([13, 26], 0) == 39)
assert(no_unlucky([13, 25], -13) == 25)
