import requests
import json


# 获取合约指数接口
class GetIndex:
    def __init__(self, name):
        if name == "usdt":
            self.url = "http://usdtfuture.test.58ex.com/usdt/market/data/get?contractId=1001"
        if name == "regular":
            self.url = "http://rusdtfuture.test.58ex.com/rusdt/market/data/get?contractId=2001"
        if name == "swap":
            self.url = "http://swapapi.test.58ex.com/market/data/get?contractId=1"

    def get_index(self):

        response = requests.get(url=self.url).json()
        # return json.dumps(response, indent=2, ensure_ascii=False)
        return response["data"]["marketData"]["indexPrice"]
