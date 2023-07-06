# Author: Sirui Ray Li
# Created: 7/5/23
# Version: 1.0
# Description:
import dataclasses
from dataclasses import dataclass
from typing import Optional, List, Union, Dict, Any

import time
import requests

from tkpysdk import create_300k_header
from tkpysdk.utils.config import BASE_URL_300K_API
from tkpysdk.utils.network import Network


def create_order(api_key: str, api_secret: str, network: Network, post_body: Dict[str, Any],
                 timeout: Optional[int] = 120000):
    """

    @param api_key:
    @param api_secret:
    @param network:
    @param post_body: In the form of CreateOrderParams {
                                                          routeHashes: string[];
                                                          expireTimestamp?: number;
                                                          gasPrice?: string;
                                                          maxPriorityFeePerGas?: string;
                                                          walletAddress: string;
                                                          amountIn: number;
                                                          amountInRaw?: string;
                                                          amountOutMin: number;
                                                          nonce?: number;
                                                          strategyId?: number;
                                                          strategyType?: number;
                                                          traderAddress: string;
                                                          newClientOrderId?: string;
                                                          dynamicGasPrice?: boolean;
                                                          estimateGasOnly?: boolean | 'skip';
                                                        }
    @param timeout:
    @return:
    """
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
