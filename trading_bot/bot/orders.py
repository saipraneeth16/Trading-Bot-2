from bot.validators import validate_inputs
from bot.logging_config import logger

def place_order(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    order_params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order_params["price"] = price
        order_params["timeInForce"] = "GTC"

    logger.info(f"Placing order: {order_params}")
    response = client.place_order(**order_params)
    logger.info(f"Order response: {response}")

    return response
