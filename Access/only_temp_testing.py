EXCHANGE_RATES = {
    "CAD": {
        "USD": 0.753,
        "JPY": 82.463,
        "EUR": 0.684,
        "GBP": 0.583
    },
    "CHF": {
        "USD": 1.001,
        "GBP": 0.776,
        "CAD": 1.330
    },
    "EUR": {
        "CHF": 1.100,
        "GBP": 0.853
    },
    "USD": {
        "EUR": 0.908,
        "GBP": 0.774,
        "JPY": 109.510
    },
    "GBP": {},
    "JPY": {
        "GBP": 0.707,
        "EUR": 0.829,
        "CHF": 0.912
    }
}

rate = EXCHANGE_RATES['CHF']['JPY']
