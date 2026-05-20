def validate_order(order_type, price):

    if order_type == "LIMIT" and not price:
        raise ValueError("LIMIT order requires price")