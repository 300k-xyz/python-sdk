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
        self.post_body = {
            'traderAddress': self.TRADER_ADDRESS,
            'walletAddress': self.WALLET_ADDRESS,
            'token0': '0x471ece3750da237f93b8e339c536989b8978a438',
            'token1': '0x765de816845861e75a25fca122bb6898b8b1282a',
            'amount0Desired': 0.001,
            'amount1Desired': 0,
            'priceLower': '0.705',
            'priceUpper': '0.95',
            'fee': 3000,
            'gasPrice': str(int(5e9)),
            'estimateGasOnly': True,
        }


if __name__ == '__main__':
    unittest.main()
