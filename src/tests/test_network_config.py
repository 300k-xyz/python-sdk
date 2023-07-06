# Author: Sirui Ray Li
# Created: 7/5/23
# Version: 1.0
# Description: test for utils
import unittest

from tkpysdk.utils.config import BASE_URL_300K_API
from tkpysdk.utils.network import get_chain_id_from_network, ChainId, get_network_from_chain_id


class TestNetworkAndConfig(unittest.TestCase):
    def test_config(self):
        self.assertEqual('https://api.300k.xyz', BASE_URL_300K_API)  # add assertion here

    def test_get_chain_id_from_network(self):
        self.assertEqual(137, ChainId.POLYGON.value)
        self.assertEqual(ChainId.POLYGON, get_chain_id_from_network('polygon'))
        self.assertEqual(43114, ChainId.AVALANCHE.value)
        self.assertEqual(ChainId.AVALANCHE, get_chain_id_from_network('avalanche'))
        self.assertEqual(1, ChainId.MAINNET.value)
        self.assertEqual(ChainId.MAINNET, get_chain_id_from_network('ethereum'))

    def test_get_chain_id_from_network_throw_error(self):
        with self.assertRaises(ValueError) as context:
            get_chain_id_from_network("invalid_network")
        self.assertTrue('getChainIdFromNetwork unsupported network' in str(context.exception))

    def test_get_network_from_chain_id(self):
        self.assertEqual('ethereum', get_network_from_chain_id(ChainId.MAINNET))
        self.assertEqual('bsc', get_network_from_chain_id(ChainId.BSC))
        self.assertEqual('celo', get_network_from_chain_id(ChainId.CELO))
        self.assertEqual('polygon', get_network_from_chain_id(ChainId.POLYGON))

    def test_get_network_from_chain_id_throw_error(self):
        invalid_chain_id = "invalid_chain_id"
        with self.assertRaises(ValueError) as context:
            get_network_from_chain_id(invalid_chain_id)
        self.assertTrue('unsupported chainId' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
