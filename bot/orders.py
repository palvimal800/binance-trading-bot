import time
import hmac
import hashlib
import requests
import os

from dotenv import load_dotenv
from bot.logging_config import logger

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://demo-fapi.binance.com"

def place_order(symbol, side, order_type, quantity, price=None):

    endpoint = "/fapi/v1/order"

    timestamp = int(time.time() * 1000)

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "timestamp": timestamp
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    query_string = "&".join([f"{k}={v}" for k, v in params.items()])

    signature = hmac.new(
        API_SECRET.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

    params["signature"] = signature

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    logger.info(f"Order Request: {params}")

    response = requests.post(
        BASE_URL + endpoint,
        headers=headers,
        params=params
    )

    logger.info(f"Response: {response.text}")

    return response.json()