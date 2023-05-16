import unittest

from src.signature import create_300k_header


class TestWindow(unittest.TestCase):
    api_key = 'test-key'
    api_secret = '9128jahjcxmi9823rXjs74S2133'
    ts = 1684209109427

    def test_simple_get(self):
        header = create_300k_header(method = 'GET', path = '/api/v1/smoke', api_key = self.api_key, api_secret = self.api_secret, post_data = None, ts = self.ts)
        self.assertDictEqual(header, {'X-APIKEY': self.api_key, 'X-TS': self.ts, 'X-SIGNATURE': 'db35e14f46f005bb15d09ce4fec9f7fd6dbb562278f708f374268dd6a01a94bf'})
        return
 
    def test_simple_post(self):
        header = create_300k_header(method = 'POST', path = '/api/v1/smoke', api_key = self.api_key, api_secret = self.api_secret, post_data = { "foo": "bar" }, ts = self.ts)
        self.assertDictEqual(header, {'X-APIKEY': self.api_key, 'X-TS': self.ts, 'X-SIGNATURE': 'ce0f653adba9df22c4b2ea0bc409250bb4d1465ba9c124a2549b0bae38cb5428'})
        return

if __name__ == "__main__":
    unittest.main()
