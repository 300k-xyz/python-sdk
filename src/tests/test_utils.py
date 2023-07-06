import time
import unittest

from tests.shared_test_setup import UnitTestBase
from tkpysdk import get_order_history, \
    create_position, \
    get_position_details, \
    get_erc20_balance, \
    get_order_book, \
    create_order, remove_liquidity_and_burn


class UnitTestUtils(UnitTestBase):

    def test_get_order_history(self):
        order_history = get_order_history(api_key=self.API_KEY,
                                          api_secret=self.API_SECRET,
                                          network=self.NETWORK,
                                          query={
                                              'walletAddress': self.WALLET_ADDRESS
                                          })
        print(order_history)
        self.assertIsNotNone(order_history)

    def test_create_position(self):
        post_body = {
            'traderAddress': self.TRADER_ADDRESS,
            'walletAddress': self.WALLET_ADDRESS,
            'token0': self.TOKEN0,
            'token1': self.TOKEN1,
            'amount0Desired': 0.001,
            'amount1Desired': 0,
            'priceLower': '0.705',
            'priceUpper': '0.95',
            'fee': 3000,
            'gasPrice': self.GAS_PRICE,
            'estimateGasOnly': True,  # set estimateGasOnly = False to actually send transactions on chain
        }
        position = create_position(api_key=self.API_KEY,
                                   api_secret=self.API_SECRET,
                                   network=self.NETWORK,
                                   post_body=post_body)
        print(position)
        self.assertIsNotNone(position)

    def test_get_position_details(self):
        position_details = get_position_details(wallet_address=self.WALLET_ADDRESS,
                                                network=self.NETWORK,
                                                api_key=self.API_KEY,
                                                api_secret=self.API_SECRET)
        print(position_details)
        self.assertIsNotNone(position_details)

    def test_remove_liquidity_and_burn(self):
        """
        Expected to be failed
        @return:
        """
        print(f'self.apikey: {self.API_KEY}')
        post_body = {
            'traderAddress': self.TRADER_ADDRESS,
            'walletAddress': self.WALLET_ADDRESS,
            'positionId': 2884,
            'gasPrice': self.GAS_PRICE,
            'estimateGasOnly': False,  # set estimateGasOnly = False to actually send transactions on chain
        }
        result = remove_liquidity_and_burn(api_key=self.API_KEY,
                                           api_secret=self.API_SECRET,
                                           network=self.NETWORK,
                                           post_body=post_body)
        print(result)


class UnitTestQuote(UnitTestBase):
    def test_get_erc20_balance(self):
        result = get_erc20_balance(network=self.NETWORK,
                                   query={
                                       'walletAddress': self.WALLET_ADDRESS,
                                       'erc20TokenAddress': self.TOKEN0,
                                   },
                                   api_secret=self.API_SECRET,
                                   api_key=self.API_KEY)
        print(result)
        self.assertIsNotNone(result)

    def test_get_order_book(self):
        result = get_order_book(network=self.NETWORK,
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


class TestSwap(UnitTestBase):

    def test_create_order(self):
        result = get_order_book(network=self.NETWORK,
                                query={
                                    'symbol': 'CELO/cUSD',
                                    'side': 'bid',
                                    'amountUSD': 100,
                                },
                                api_secret=self.API_SECRET,
                                api_key=self.API_KEY)
        order_book = result
        ask_price = order_book['bids'][0][0]
        allowed_slippage = 0.001  # Replace with the actual value
        wallet_address = self.WALLET_ADDRESS  # Replace with the actual value
        amount_in = 200  # Replace with the actual value
        trader_address = self.TRADER_ADDRESS  # Replace with the actual value
        post_body = {
            'routeHashes': [order_book['bids'][0][2]],
            'expireTimestamp': int(time.time() + 12),
            'walletAddress': wallet_address,
            'amountIn': amount_in,
            'amountOutMin': (amount_in / ask_price) * (1 - allowed_slippage),
            'strategyId': 1,
            'strategyType': 2,
            'traderAddress': trader_address,
            'newClientOrderId': f"test-{int(time.time())}",
            'dynamicGasPrice': False,
            'estimateGasOnly': True  # set estimateGasOnly = False to actually send transactions on chain
        }
        result = create_order(api_key=self.API_KEY,
                              api_secret=self.API_SECRET,
                              network=self.NETWORK,
                              post_body=post_body)
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
