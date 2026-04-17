from binance.client import Client

def get_client(api_key, api_secret):
    client = Client(
        api_key,
        api_secret,
        testnet=True
    )

    client.recvWindow = 10000

    return client