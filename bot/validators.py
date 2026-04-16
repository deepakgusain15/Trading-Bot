def validate_input(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and not price:
        raise ValueError("Price is required for LIMIT orders")