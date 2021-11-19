def multiples_of(n, count):
    if not isinstance(count,int) or count<0:
        return False
    dict = {}
    for i in range(1,count+1):
        dict.update({i:i*n})
    return dict

assert(multiples_of(3, 4)  == {1: 3, 2: 6, 3: 9, 4: 12})
assert(multiples_of(2, 0)  == {})
assert(multiples_of(0, 3)  == {1: 0, 2: 0, 3: 0})
assert(multiples_of(-2, 3) == {1: -2, 2: -4, 3: -6})
assert(multiples_of(5, -5) == False)
assert(multiples_of(5, "bruh") == False)
