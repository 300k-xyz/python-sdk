import unittest
from dotenv import load_dotenv
import os

from tkpysdk.utils.network import Network
from tkpysdk.utils.order_utils import get_order_history

load_dotenv(dotenv_path="../../../../.env")


class TestOrderUtils(unittest.TestCase):
    def setUp(self):
        self.WALLET_ADDRESS = os.getenv('walletAddress')
        self.TRADER_ADDRESS = os.getenv('traderAddress')
        self.API_KEY = os.getenv('apiKey')
        self.API_SECRET = os.getenv('apiSecret')

    def test_order_utils(self):
        print(get_order_history(api_key=self.API_KEY,
                                api_secret=self.API_SECRET,
                                network=Network.ethereum,
                                query={
                                    'walletAddress': self.WALLET_ADDRESS
                                }))

if __name__ == '__main__':
    unittest.main()
