import logging

class OrderManager:
    def __init__(self, client):
        self.client = client.client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            logging.info(f"Placing order: {symbol} {side} {order_type} {quantity}")
            logging.info(f"Response: {order}")

            return order

        except Exception as e:
            logging.error(str(e))
            return {"error": str(e)}