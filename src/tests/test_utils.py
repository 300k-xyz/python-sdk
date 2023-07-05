import unittest

from tests.shared_test_setup import TestSetUp
from tkpysdk.utils.network import Network
from tkpysdk.utils.order_utils import get_order_history
from tkpysdk.utils.position_utils import create_position, CreatePositionResponse, get_position_details, \
    remove_liquidity_and_burn


class TestUtils(TestSetUp):

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
    
if __name__ == '__main__':
    unittest.main()
