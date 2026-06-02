def validate_inputs(symbol, side, order_type, quantity, price=None):

    side = side.upper()
    order_type = order_type.upper()
    symbol = symbol.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")

    return True
