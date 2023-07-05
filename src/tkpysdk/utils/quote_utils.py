# Author: Sirui Ray Li
# Created: 7/5/23
# Version: 1.0
# Description:

import time
from dataclasses import dataclass

import requests
from typing import Optional, Tuple, List, Dict

from tkpysdk import create_300k_signature
from tkpysdk.utils.config import BASE_URL_300K_API
from tkpysdk.utils.network import Network


QuoteArr = Tuple[float, float, str, str, float]


@dataclass
class OrderbookResponse:
    symbol: str
    amount_usd: float
    last_update_ts: int
    asks: Optional[List[QuoteArr]] = None
    bids: Optional[List[QuoteArr]] = None


def get_erc20_balance(api_key: str, api_secret: str, network: Network, query: Dict[str, str]) -> str:
    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/get-balance"
    url = f"{BASE_URL_300K_API}{path}"
    headers = {
        'X-APIKEY': api_key,
        'X-TS': str(ts),
        'X-SIGNATURE': create_300k_signature(ts, 'GET', path, api_secret, {})
    }
    res = requests.get(url, params=query, headers=headers)
    return res.json()


def get_order_book(api_key: str, api_secret: str, network: Network, query: Dict[str, any]) -> OrderbookResponse:
    """

    @param api_key:
    @param api_secret:
    @param network:
    @param query: format:
                    {
                    symbol: string;
                    side: 'bid' | 'ask';
                    // if LINK/USDC, can use amountUSD to specify how much USD trade to quote
                    amountUSD?: number;
                    // if LINK/WETH, can use amountQuote to specify how much WETH worth of trade to quote
                    amountQuote?: number;
                  }
    @return:
    """

    ts = int(time.time() * 1000)
    path = f"/api/{network.value}/v1/rfq/orderbook"
    url = f"{BASE_URL_300K_API}{path}"
    headers = {
        'X-APIKEY': api_key,
        'X-TS': str(ts),
        'X-SIGNATURE': create_300k_signature(ts, 'GET', path, api_secret, {})
    }
    amount_usd = query.get('amountUSD')
    amount_quote = query.get('amountQuote')
    if not amount_usd and not amount_quote:
        raise ValueError("either amountQuote or amountUSD is required")
    res = requests.get(url, params=query, headers=headers)
    return res.json()
