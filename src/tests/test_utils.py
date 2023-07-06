import time
import unittest

from tests.shared_test_setup import UnitTestBase
from tkpysdk.utils.network import Network
from tkpysdk.utils.order_utils import get_order_history
from tkpysdk.utils.position_utils import create_position, get_position_details, \
    remove_liquidity_and_burn
from tkpysdk.utils.quote_utils import get_erc20_balance, get_order_book
from tkpysdk.utils.swap_utils import create_order


class UnitTestUtils(UnitTestBase):

    def test_order_utils(self):
        print(get_order_history(api_key=self.API_KEY,
                                api_secret=self.API_SECRET,
                                network=Network.celo,
                                query={
                                    'walletAddress': self.WALLET_ADDRESS
                                }))

    def test_position_utils(self):
        position = create_position(api_key=self.API_KEY,
                                   api_secret=self.API_SECRET,
                                   network=Network.celo,
                                   post_body=self.post_body)
        print(position)
        self.assertIsNotNone(position)

    def test_position_detail(self):
        position_details = get_position_details(wallet_address=self.WALLET_ADDRESS,
                                                network=Network.celo,
                                                api_key=self.API_KEY,
                                                api_secret=self.API_SECRET)
        print(position_details)
        self.assertIsNotNone(position_details)
    # def test_remove_liquidity_and_burn(self):
    #     print(f'self.apikey: {self.API_KEY}')
    #     post_body = {
    #         'traderAddress': self.TRADER_ADDRESS,
    #         'walletAddress': self.WALLET_ADDRESS,
    #         'positionId': 2884,
    #         'gasPrice': str(int(5e9)),
    #         'estimateGasOnly': False,
    #     }
    #     result = remove_liquidity_and_burn(api_key=self.API_KEY,
    #                                        api_secret=self.API_SECRET,
    #                                        network=Network.celo,
    #                                        post_body=post_body)
    #     print(result)
    #     self.assertIsNotNone(result)


class UnitTestQuote(UnitTestBase):
    def test_get_erc20_balance(self):
        result = get_erc20_balance(network=Network.celo,
                                   query={
                                       'walletAddress': '0x6453cD5b57576548556e872029dD86e210016965',
                                       'erc20TokenAddress': '0x471ece3750da237f93b8e339c536989b8978a438',
                                   },
                                   api_secret=self.API_SECRET,
                                   api_key=self.API_KEY)
        print(result)
        self.assertIsNotNone(result)

    def test_get_order_book(self):
        result = get_order_book(network=Network.celo,
                                query={
                                    'symbol': 'CELO/cUSD',
                                    'side': 'bid',
                                    'amountUSD': 100,
                                },
                                api_secret=self.API_SECRET,
                                api_key=self.API_KEY)
        self.order_book = result
        print(f'result: {result}')
        self.assertIsNotNone(result)


class TestSwap(UnitTestQuote):

    def test_create_order(self):
        self.test_get_order_book()
        ask_price = self.order_book['bids'][0][0]
        allowed_slippage = 0.001  # Replace with the actual value
        wallet_address = self.WALLET_ADDRESS  # Replace with the actual value
        amount_in = 200  # Replace with the actual value
        trader_address = self.TRADER_ADDRESS  # Replace with the actual value
        post_body = {
            'routeHashes': [self.order_book['bids'][0][2]],
            'expireTimestamp': int(time.time() + 12),
            'walletAddress': wallet_address,
            'amountIn': amount_in,
            'amountOutMin': (amount_in / ask_price) * (1 - allowed_slippage),
            'strategyId': 1,
            'strategyType': 2,
            'traderAddress': trader_address,
            'newClientOrderId': f"test-{int(time.time())}",
            'dynamicGasPrice': False,
            'estimateGasOnly': True
        }
        result = create_order(api_key=self.API_KEY,
                              api_secret=self.API_SECRET,
                              network=Network.celo,
                              post_body=post_body)
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
