# Author: Sirui Ray Li
# Created: 7/5/23
# Version: 1.0
# Description:
import dataclasses
from dataclasses import dataclass
from typing import Optional, List, Union

import time
import requests

from tkpysdk import create_300k_header
from tkpysdk.utils.config import BASE_URL_300K_API
from tkpysdk.utils.network import Network


@dataclass
class CreateOrderParams:
    route_hashes: List[str]
    wallet_address: str
    amount_in: float
    amount_out_min: float
    trader_address: str
    expire_timestamp: Optional[int] = None
    gas_price: Optional[str] = None
    max_priority_fee_per_gas: Optional[str] = None
    amount_in_raw: Optional[str] = None
    nonce: Optional[int] = None
    strategy_id: Optional[int] = None
    strategy_type: Optional[int] = None
    new_client_order_id: Optional[str] = None
    dynamic_gas_price: Optional[bool] = None
    estimate_gas_only: Optional[Union[bool, str]] = None


def create_order(api_key: str, api_secret: str, network: Network, post_body: CreateOrderParams,
                 timeout: Optional[int] = 120000):
    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/order"
    url = f"{BASE_URL_300K_API}{path}"

    headers = create_300k_header(ts=ts,
                                 method='POST',
                                 path=path,
                                 api_key=api_key,
                                 api_secret=api_secret,
                                 post_data=post_body)
    res = requests.post(url, json=post_body, timeout=timeout / 1000, headers=headers)
    return res.json()
