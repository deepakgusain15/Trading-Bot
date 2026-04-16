import argparse
from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_input
from bot.logging_config import setup_logger
import logging

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

try:
    validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

    client = BinanceClient()
    order_manager = OrderManager(client)

    order = order_manager.place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    if "error" in order:
        print(" Failed:", order["error"])
    else:
        print("\n Order Summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        print("\n Response")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")

    logging.info(order)

except Exception as e:
    print("Error:", e)
    logging.error(str(e))