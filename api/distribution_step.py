import requests
import json
class dis_step():
    def __init__(self):
        self.url ='http://saasapi.fhd001.com'
        self.referer='fhdportal'
        self.shopid ='wxd3b600b271b704f1'
        self.platform ='ec'
        self.marsid ='561'
        self.marsCode = 'RJ7AT'
        self.token = '~VVYDAgBWBhxSGAJTTwBSSQUYWh0HAkhUABhUTQJIUA5cUQcABV8GAB1RVQg%3D~1~'
        self.headers = {'Content-Type':'application/x-www-form-urlencoded'}
    def session(self):
        self.s = requests.session()
        self.s.headers.update(self.headers)
        return self.s
    def request(self,method,url,params =None):
        try:
            # 判断请求方法
            if method == "get":
                self.result = requests.get(url=url, params=params).json()
            elif method == "post":
                if "application/json" in self.headers:
                    self.result = self.s.post(url=url, json=params).json()
                else:
                    self.result = self.s.post(url=url, data=params).json()
            else:
                print("其他请求放式")
            return self.result
        except Exception as e:
            print("http请求报错：%s" % e)


    #分页查询分销订单信息
    def get_query_order_data(self,status):
        path = '/api/distribution/order/queryDistributionOrderPaging'
        Request_URL = self.url+path
        params={
            'shopId':self.shopid,
            'platform':self.platform,
            'status':status, #订单状态( 1-待分配；2-已分配未发货；3-已分配已发货)
            'useTimeInt':1,
            'sort':'payTime',
            'desc':'true',
            'page':1,
            'pageSize':1,
            'referer':self.referer,
            'token':self.token
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)
        self.distributionOrderSn = data['distributionOrderSn']
        self.orderSn = data['orderSn']
        return self.distributionOrderSn,self.orderSn

        # 获取自动分销规则配置

    def get_configuration(self):
        path = '/api/distribution/factory/getDistributionRule'
        Request_URL = self.url + path
        params = {
            'shopIds': self.shopid,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)
        self.cofing_data = data['data']
        return self.cofing_data

        # 保存自动分销配置

    def save_configuration(self):
        path = '/api/distribution/factory/saveDistributionRule'
        Request_URL = self.url + path
        params = {
            'configStr': self.cofing_data,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 分销订单

    def disibute_Orders(self):
        path = '/api/distribution/order/disibuteOrder'
        Request_URL = self.url + path
        query_data = self.get_query_order_data(1)
        orderListStr = {
            'distributionOrderSn': query_data[0],
            'orderSn': query_data[1]
        }
        params = {
            'shopId': self.shopid,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token,
            'orderListStr': [orderListStr],
            'marsId': self.marsid,
            'marsCode': self.marsCode
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 取消分销订单

    def cancel_Orders(self):
        path = '/api/distribution/order/disibuteOrder'
        Request_URL = self.url + path
        query_data = self.get_query_order_data(2)
        orderListStr = {
            'distributionOrderSn': query_data[0],
            'orderSn': query_data[1]
        }
        params = {
            'shopId': self.shopid,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token,
            'orderListStr': [orderListStr],
            'marsId': self.marsid,
            'marsCode': self.marsCode
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 判断回传的订单是否为分销订单

    def assess_orders(self):
        path = '/api/distribution/order/isDistributionOrder'
        Request_URL = self.url + path
        params = {
            'orderSns': '3713222212395599872',
            'shopId': self.shopid,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 生成邀请厂家链接

    def get_Manufacturer_Link(self):
        path = '/api/distribution/factory/generateInviteLink'
        Request_URL = self.url + path
        shopToken = [{'shopId': self.shopid, 'shopName': 'Harryyoo'}]
        params = {
            'shopToken': shopToken,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 取消绑定厂家的前置操作

    def check_Distribution_Order(self):
        path = '/api/distribution/order/checkDistributionOrder'
        Request_URL = self.url + path
        params = {
            'shopId': self.shopid,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token,
            'marsId': self.marsid
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 分页查询商品分销商品信息

    def query_DistributionItem(self):
        path = '/api/distribution/item/queryDistributionItem'
        Request_URL = self.url + path
        params = {
            'shopId': self.shopid,
            'platform': self.platform,
            'referer': self.referer,
            'token': self.token,
            'page': 1,
            'pageSize': 10
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 根据分销商品ID查询对应的SKU信息

    def query_sku_data(self):
        path = '/api/distribution/item/queryDistributionItemSkuByItemIdList'
        Request_URL = self.url + path
        params = {
            'shopId': self.shopid,
            'platform': self.platform,
            'itemIds': 10000000808897,
            'token': self.token,
            'referer': self.referer,

        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)

        # 将分销商品与厂家绑定

    def bind_DistributionItem_Factory(self):
        path = '/api/distribution/item/bindDistributionItemFactory'
        Request_URL = self.url + path
        params = {
            'shopId': self.shopid,
            'platform': self.platform,
            'referer': self.referer,
            'itemIds': 10000000808897,
            'token': self.token,
            'marsId': self.marsid,
        }
        self.result = self.request('post', Request_URL, params)
        data = json.loads(self.result)



