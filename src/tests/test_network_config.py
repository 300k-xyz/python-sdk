# Author: Sirui Ray Li
# Created: 7/5/23
# Version: 1.0
# Description: test for utils
import unittest

from tkpysdk.utils.config import BASE_URL_300K_API
from tkpysdk.utils.network import get_chain_id_from_network, Network, ChainId, get_network_from_chain_id


class TestNetworkAndConfig(unittest.TestCase):
    def test_config(self):
        self.assertEqual('https://api.300k.xyz', BASE_URL_300K_API)  # add assertion here

    def test_network(self):
        # Test get_chain_id_from_network
        self.assertEqual(137, ChainId.POLYGON.value)
        self.assertEqual(ChainId.POLYGON, get_chain_id_from_network(Network.polygon))
        self.assertEqual(43114, ChainId.AVALANCHE.value)
        self.assertEqual(ChainId.AVALANCHE, get_chain_id_from_network(Network.avalanche))
        self.assertEqual(1, ChainId.MAINNET.value)
        self.assertEqual(ChainId.MAINNET, get_chain_id_from_network(Network.ethereum))
        # Test throw error
        with self.assertRaises(ValueError) as context:
            get_chain_id_from_network("Ray's RandomID")
        self.assertTrue('getChainIdFromNetwork unsupported network' in str(context.exception))

        # Test get_network_from_chain_id
        self.assertEqual('ethereum', Network.ethereum.value)
        self.assertEqual('ethereum', get_network_from_chain_id(ChainId.MAINNET).value)
        self.assertEqual('bsc', get_network_from_chain_id(ChainId.BSC).value)
        self.assertEqual('celo', get_network_from_chain_id(ChainId.CELO).value)
        self.assertEqual('polygon', get_network_from_chain_id(ChainId.POLYGON).value)
        # Test throw error
        with self.assertRaises(ValueError) as context:
            get_network_from_chain_id("randomtestingstringrayishandsome")
        self.assertTrue('unsupported chainId' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
