def bill(per_hour, parts_prices_hours):
    total_cost = 0
    one_none = False
    for key in parts_prices_hours:
        tup = parts_prices_hours.get(key)
        part_price = tup[0]
        part_hours = tup[1]
        if part_price is None:
            part_price = 0
            one_none = True
        if part_hours is None:
            part_hours = 1
            one_none = True
        total_cost += part_price + part_hours*per_hour
    ret_tup = (total_cost, one_none)
    return ret_tup


assert(bill(0, {'Door': (23.33, 2.50)}) == (23.33, False))
assert(bill(0, {}) == (0, False))
assert(bill(0, {'Door': (None, 3.0)}) == (0, True))
assert(bill(50, {'Door': (None, 3.0)}) == (150, True))
assert(bill(50, {'Door': (10, None)}) == (60, True))
assert(bill(10.5, {'Door': (None, 3.0), 'Window': (22.22, 0.5)}) == (58.97, True))
assert(bill(10.5, {'Window': (22.22, 0.5)}) == (27.47, False))
