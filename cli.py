from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logging

API_KEY = "ENTER YOUR API KEY HERE"
API_SECRET = "ENTER YOUR API SECRET KEY HERE"

def main():
    setup_logging()

    try:
        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        side = input("Enter side (BUY/SELL): ").upper()
        order_type = input("Enter type (MARKET/LIMIT): ").upper()
        quantity = float(input("Enter quantity: "))

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        price = None
        if order_type == "LIMIT":
            price = input("Enter price: ")

        client = get_client(API_KEY, API_SECRET)

        order = place_order(client, symbol, side, order_type, quantity, price)

        print("\n✅ Order placed successfully!")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))

    except Exception as e:
        print("\n❌ Error:", e)

if __name__ == "__main__":
    main()