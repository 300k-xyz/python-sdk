# 300k-python-sdk

pip install git+https://github.com/300k-xyz/python-sdk.git#egg=tkpysdk
 
 ### usage
```
from tkpysdk import create_300k_header

create_300k_header("POST", path = "/api/v1/smoke", api_key = "x", api_secret = "y", post_data = {})

# output:
# {'X-APIKEY': 'x', 'X-TS': 1684251958440, 'X-SIGNATURE': '4fab963b64bc9a89e979596a8714db7cdb3bf79d806b6fb146ecf62f1632b5ea'}

```
