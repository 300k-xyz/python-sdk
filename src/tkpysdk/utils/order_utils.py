# Author: Sirui Ray Li
# Created: 7/5/23
# Version: 1.0
# Description:
import time
from typing import Dict, Optional, Union
from urllib.parse import urljoin
import requests
from tkpysdk import create_300k_signature
from tkpysdk.utils.config import BASE_URL_300K_API
from tkpysdk.utils.network import Network


def get_order_history(
        api_key: str,
        api_secret: str,
        network: Network,
        query: Dict[str, Optional[Union[str, int]]]
):
    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/history-orders"
    url = urljoin(BASE_URL_300K_API, path)
    headers = {
        'X-APIKEY': api_key,
        'X-TS': str(ts),
        'X-SIGNATURE': create_300k_signature(ts, 'GET', path, api_secret, query),
    }
    res = requests.get(url, params=query, headers=headers)
    return res.json()
