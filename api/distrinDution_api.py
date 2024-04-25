from common.request_tools import requests_data
from common.yaml_tools import updata_case


class distrindution:

    # 分页查询分销订单信息
    @classmethod
    def get_query_order_data(csl,yaml_path, case_name,config_url):
        result = requests_data(yaml_path, case_name,config_url)
        # print('查询分销订单信息的内容',result.json())
        data = result.json()['data']['list'][0]
        distributionOrderSn = data['distributionOrderSn']
        orderSn = data['orderSn']
        orderListStr = [{'distributionOrderSn': distributionOrderSn,'orderSn': orderSn}]
        updata_case(yaml_path,'orderListStr',str(orderListStr))
        updata_case(yaml_path,'orderSns',orderSn)
        return result
    #获取自动分销规则配置
    @classmethod
    def get_configuration(csl,yaml_path,case_name,config_url):
        result = requests_data(yaml_path,case_name, config_url)
        cofing_data = result.json()['data']
        updata_case(yaml_path,'configStr',cofing_data)
        return result
    #查询售卖中的商品信息
    @classmethod
    def query_items_data(cls,yaml_path,case_name,config_url):
        result = requests_data(yaml_path,case_name,config_url)
        items_data = result.json()['data']['list'][0]['itemId']
        updata_case(yaml_path,'itemIds',items_data)
        return result

    # 根据分销商品ID查询对应的SKU信息
    @classmethod
    def query_sku_data(csl,yaml_path,case_name,config_url):
        result = requests_data(yaml_path,case_name,config_url)
        return result
   #保存自动分销配置
    @classmethod
    def save_configuration(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        return result
#
#
#    #分销订单
    @classmethod
    def disibute_Orders(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result
#
#     #取消分销订单
    @classmethod
    def cancel_Orders(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result
#
    #判断回传的订单是否为分销订单
    @classmethod
    def assess_orders(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result

#    #生成邀请厂家链接
    @classmethod
    def get_Manufacturer_Link(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result
#
#   #取消绑定厂家的前置操作
    @classmethod
    def check_Distribution_Order(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result


#
#     #分页查询商品分销商品信息分销商品页面
    @classmethod
    def query_DistributionItem(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        items_data = result.json()['data']['list'][0]['itemId']
        updata_case(yaml_path,'itemIds',items_data)
        return result

    #将分销商品与厂家绑定
    @classmethod
    def bind_DistributionItem_Factory(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result



    #查询最后同步任务-订单
    @classmethod
    def query_Lates_SyncTask01_orders(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result
    #最新的同步任务-订单
    @classmethod
    def query_Lates_SyncTask2_orders(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        data = result.json()['data']
        id = data['id']
        params = data['params']
        updata_case(yaml_path,'id',id)
        updata_case(yaml_path,'params',params)
        return result
    #保存任务-订单
    @classmethod
    def save_Sync_Task_orders(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result
    #查询任务—订单
    @classmethod
    def query_Sync_Task_Progress_orders(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result



    #查询最后同步任务-订单
    @classmethod
    def query_Lates_SyncTask01_goods(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result
    #最新的同步任务-订单
    @classmethod
    def query_Lates_SyncTask2_goods(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)

        data = result.json()['data']
        print(result.json())
        print(data)
        id = data['id']
        params = data['params']
        updata_case(yaml_path,'id',id)
        updata_case(yaml_path,'params',params)
        return result
    #保存任务-订单
    @classmethod
    def save_Sync_Task_goods(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result
    #查询任务—订单
    @classmethod
    def query_Sync_Task_Progress_goods(csl,yaml_path, case_name, config_url):
        result = requests_data(yaml_path, case_name, config_url)
        print(result.json())
        return result