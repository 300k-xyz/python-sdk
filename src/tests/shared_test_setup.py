import unittest
from dotenv import load_dotenv
import os


class TestSetUp(unittest.TestCase):
    def setUp(self):
        load_dotenv(dotenv_path="../../.env")
        self.WALLET_ADDRESS = os.getenv('walletAddress')
        self.TRADER_ADDRESS = os.getenv('traderAddress')
        self.API_KEY = os.getenv('apiKey')
        self.API_SECRET = os.getenv('apiSecret')


if __name__ == '__main__':
    unittest.main()
