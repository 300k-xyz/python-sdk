import unittest
from dotenv import load_dotenv
import os


class UnitTestBase(unittest.TestCase):
    def setUp(self):
        load_dotenv(dotenv_path="../../.env")
        self.WALLET_ADDRESS = os.getenv('walletAddress')
        self.TRADER_ADDRESS = os.getenv('traderAddress')
        self.API_KEY = os.getenv('apiKey')
        self.API_SECRET = os.getenv('apiSecret')
        self.NETWORK = 'celo'
        self.TOKEN0 = '0x471ece3750da237f93b8e339c536989b8978a438'
        self.TOKEN1 = '0x765de816845861e75a25fca122bb6898b8b1282a'
        self.GAS_PRICE = str(int(5e9))


if __name__ == '__main__':
    unittest.main()
