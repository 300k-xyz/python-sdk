# Author: Sirui Ray Li
# Created: 7/5/23
# Version: 1.0
# Description:

from dataclasses import dataclass
from typing import Any, Optional, Dict, List
import time
import requests

from tkpysdk import create_300k_header
from tkpysdk.utils.config import BASE_URL_300K_API
from tkpysdk.utils.network import Network


@dataclass
class V3Position:
    tokenId: int
    nonce: str
    operator: str
    token0: str
    token1: str
    fee: int
    tickLower: int
    tickUpper: int
    liquidity: str
    feeGrowthInside0LastX128: str
    feeGrowthInside1LastX128: str
    tokensOwed0: str
    tokensOwed1: str
    token0Symbol: str
    token1Symbol: str
    token0Decimals: int
    token1Decimals: int
    priceLower: str
    priceUpper: str
    priceLowerInvert: str
    priceUpperInvert: str
    amount0: str
    amount1: str
    sqrtPriceX96: str
    tick: int
    poolAddress: str


@dataclass
class CreatePositionResponse:
    blockHash: str
    blockNumber: int
    contractAddress: Any
    cumulativeGasUsed: int
    effectiveGasPrice: int
    from_: str  # 'from' is a reserved keyword in Python, hence the underscore
    gasUsed: int
    logsBloom: str
    status: bool
    to: str
    transactionHash: str
    transactionIndex: int
    type_: str  # 'type' is a reserved keyword in Python, hence the underscore
    events: Any


def create_position(api_key: str,
                    api_secret: str,
                    network: Network,
                    post_body: Dict[str, any]) -> CreatePositionResponse:
    """

    @param api_key:
    @param api_secret:
    @param network:
    @param post_body: format: {
                                traderAddress: string;
                                walletAddress: string;
                                token0: string;
                                token1: string;
                                amount0Desired: number;
                                amount1Desired: number;
                                priceLower: string;
                                priceUpper: string;
                                fee: number;
                                burnPositionId?: number;
                                newClientOrderId?: string;
                                gasPrice?: string;
                                maxPriorityFeePerGas?: string;
                                estimateGasOnly?: boolean;
                                strategyId?: number;
                                strategyType?: number;
                              }
    @return:
    """
    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/v3-position"
    url = f"{BASE_URL_300K_API}{path}"
    headers = create_300k_header(ts=ts,
                                 method='POST',
                                 path=path,
                                 api_key=str(api_key),
                                 api_secret=str(api_secret),
                                 post_data=post_body)
    res = requests.post(url, json=post_body, headers=headers, timeout=120)
    return res.json()


def get_position_detail(network: Network,
                        token_id: int,
                        api_key: str,
                        api_secret: str) -> V3Position:
    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/v3-position-detail"
    url = f"{BASE_URL_300K_API}{path}?tokenId={token_id}"
    headers = create_300k_header(ts=ts,
                                 method='GET',
                                 path=path,
                                 api_key=api_key,
                                 api_secret=api_secret,
                                 post_data={})
    res = requests.get(url, headers=headers)
    return res.json()


def get_position_details(network: Network,
                         wallet_address: str,
                         api_key: str,
                         api_secret: str) -> List[V3Position]:
    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/v3-positions"
    url = f"{BASE_URL_300K_API}{path}?walletAddress={wallet_address}"
    headers = create_300k_header(ts=ts, method='GET',
                                 path=path,
                                 api_key=api_key,
                                 api_secret=api_secret,
                                 post_data={})
    res = requests.get(url, headers=headers)
    return res.json()


def remove_liquidity_and_burn(api_key: str, api_secret: str, network: Network, post_body: Dict[str, any]):
    """

    @param api_key:
    @param api_secret:
    @param network:
    @param post_body: format: {
                                positionId: number;
                                walletAddress: string;
                                traderAddress: string;
                                newClientOrderId?: string;
                                nonce?: number;
                                gasPrice?: string;
                                maxPriorityFeePerGas?: string;
                                estimateGasOnly?: boolean;
                                strategyId?: number;
                                strategyType?: number;
                              }
    @return:
    """
    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/remove-v3-position"
    url = f"{BASE_URL_300K_API}{path}"
    headers = create_300k_header(ts=ts,
                                 method='POST',
                                 path=path,
                                 api_key=api_key,
                                 api_secret=api_secret,
                                 post_data=post_body)
    res = requests.post(url, json=post_body, headers=headers, timeout=120)
    return res.json()
