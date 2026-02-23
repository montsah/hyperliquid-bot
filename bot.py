import time
import os
from datetime import datetime
from hyperliquid.info import Info
from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants

# ================== CONFIG ==================
IS_TESTNET = os.getenv('IS_TESTNET', 'true').lower() == 'true'
API_WALLET_PRIVATE_KEY = os.getenv('HYPERLIQUID_PRIVATE_KEY')  # API wallet private key
MAIN_WALLET_ADDRESS = os.getenv('HYPERLIQUID_ADDRESS')         # Your main wallet address
DRY_RUN = os.getenv('DRY_RUN', 'true').lower() == 'true'
# ===========================================

# Choose testnet or mainnet
url = constants.TESTNET_API_URL if IS_TESTNET else constants.API_URL
info = Info(url, skip_ws=True)

# Initialize exchange (this signs with your private key)
exchange = Exchange(
    wallet=API_WALLET_PRIVATE_KEY,
    base_url=url,
    account_address=MAIN_WALLET_ADDRESS
)

print(f"✅ Hyperliquid Bot started - Testnet: {IS_TESTNET} | DRY_RUN: {DRY_RUN}")

while True:
    try:
        # Example: Get current BTC price
        mid_price = info.all_mids()["BTC"]
        print(f"[{datetime.now()}] BTC Mid Price: ${mid_price}")

        # Add your strategy logic here later (VWAP, scalper, etc.)

        if not DRY_RUN:
            # Example market buy (uncomment when ready)
            # response = exchange.market_open("BTC", is_buy=True, sz=0.01)
            # print("Order placed:", response)
            pass

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(30)  # check every 30 seconds
