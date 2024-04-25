import pytest
from api.distrinDution_api import distrindution
from common.assert_tools import assert_steps





dis = distrindution
class TestShippedOrders():
    """
    查询已发货订单信息
    """
    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','get_query_order_data3')])
    def test_get_query_order_data(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.get_query_order_data(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)


if __name__ == '__main__':
    pytest.main(['-s',r'./test_query_Shipped_orders.py'])