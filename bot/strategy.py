def simple_strategy(price):
    if price < 100000:
        return "BUY"
    return "SELL"