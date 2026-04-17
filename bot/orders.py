import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Request: {side} {symbol} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            if side == "BUY":
                order = client.order_market_buy(symbol=symbol, quantity=quantity)
            else:
                order = client.order_market_sell(symbol=symbol, quantity=quantity)

        elif order_type == "LIMIT":
            if not price:
                raise ValueError("Price required for LIMIT order")

            if side == "BUY":
                order = client.order_limit_buy(
                    symbol=symbol,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )
            else:
                order = client.order_limit_sell(
                    symbol=symbol,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

        logging.info(f"Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise