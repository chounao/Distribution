from api.platform_api import update_case
from common.SingLeton_tools import MySingleton
from common.yaml_tools import updata_case_for_casename

#相同平台订单和商品对应的TYPE是不一样的所以写成两个方法
parameter = 'type'
def update_for_orders(data):
    updata_case_for_casename('distrindution_path', 'query_Lates_SyncTask01_orders', parameter, data)
    updata_case_for_casename('distrindution_path', 'query_Lates_SyncTask2_orders', parameter, data)
    updata_case_for_casename('distrindution_path', 'save_Sync_Task_orders', parameter, data)
    updata_case_for_casename('distrindution_path', 'query_Sync_Task_Progress_orders', parameter, data)
def update_for_goods(data):
    updata_case_for_casename('distrindution_path', 'query_Lates_SyncTask01_goods', parameter, data)
    updata_case_for_casename('distrindution_path', 'query_Lates_SyncTask2_goods', parameter, data)
    updata_case_for_casename('distrindution_path', 'save_Sync_Task_goods', parameter, data)
    updata_case_for_casename('distrindution_path', 'query_Sync_Task_Progress_goods', parameter, data)


def steps(platform):
    update_case(platform) #执行common.platform.py内的操作
    singleton = MySingleton.get_instance()
    if platform == "抖音":
        singleton.set_data('url','Fxg_URL')#把对应的url存起来
        orders_type = 70
        goods_type = 71
        update_for_orders(orders_type) #根据对应的平台更新测试用例
        update_for_goods(goods_type)
    elif platform == '快手':
        singleton.set_data('url', 'Other_URL')
        orders_type = 68
        goods_type = 69
        update_for_orders(orders_type)
        update_for_goods(goods_type)
    elif platform == '视频号':
        singleton.set_data('url', 'Other_URL')
        orders_type = 74
        goods_type = 75
        update_for_orders(orders_type)
        update_for_goods(goods_type)
    elif platform == '小红书':
        singleton.set_data('url', 'Other_URL')
        orders_type = 77
        goods_type = 78
        update_for_orders(orders_type)
        update_for_goods(goods_type)