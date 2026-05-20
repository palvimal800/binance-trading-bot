import argparse
import json

from bot.orders import place_order
from bot.validators import validate_order

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    validate_order(args.type, args.price)

    response = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\nOrder Successful\n")
    print(json.dumps(response, indent=4))

except Exception as e:
    print("\nOrder Failed")
    print(str(e))