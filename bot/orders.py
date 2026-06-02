from bot.client import get_client
from bot.logging_config import setup_logger


logger = setup_logger()


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        client = get_client()

        logger.info(
            f"Order Request -> Symbol:{symbol}, Side:{side}, Type:{order_type}, Qty:{quantity}, Price:{price}"
        )

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order Response -> {order}")

        return {
            "success": True,
            "data": order
        }

    except Exception as e:
        logger.error(f"Order Error -> {str(e)}")

        return {
            "success": False,
            "error": str(e)
        }
