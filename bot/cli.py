import argparse
from bot.orders import place_order
from bot.validators import validate_inputs


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.price:
            print(f"Price: {args.price}")

        result = place_order(
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\n===== ORDER RESPONSE =====")

        if result["success"]:
            data = result["data"]

            print(f"Order ID: {data.get('orderId')}")
            print(f"Status: {data.get('status')}")
            print(f"Executed Qty: {data.get('executedQty')}")
            print(f"Avg Price: {data.get('avgPrice')}")

            print("\n✅ Order placed successfully")

        else:
            print(f"\n❌ Failed: {result['error']}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
