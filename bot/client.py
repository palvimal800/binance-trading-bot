from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

client = Client(
    api_key,
    api_secret,
    testnet=True
)

client.API_URL = "https://testnet.binancefuture.com"