#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES


def convert(amount, from_currency, to_currency):
    if not (isinstance(amount, int) or isinstance(amount, float)):
        raise Warning("The given Amount is not a number")
    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        raise Warning("One of the currencies or both are not available")
    try:
        ex_rate = EXCHANGE_RATES[from_currency][to_currency]
    except KeyError:
        ex_rate = 1 / EXCHANGE_RATES[to_currency][from_currency]
    except:
        raise Warning('Something else is wrong')

    return amount * ex_rate
