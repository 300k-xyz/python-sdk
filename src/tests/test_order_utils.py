import unittest

from tests.shared_test_setup import TestSetUp
from tkpysdk.utils.network import Network
from tkpysdk.utils.order_utils import get_order_history


class TestOrderUtils(TestSetUp):

    def test_order_utils(self):
        print(get_order_history(api_key=self.API_KEY,
                                api_secret=self.API_SECRET,
                                network=Network.celo,
                                query={
                                    'walletAddress': self.WALLET_ADDRESS
                                }))


if __name__ == '__main__':
    unittest.main()
