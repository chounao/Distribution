import pytest
from api.distrinDution_api import distrindution
from common.assert_tools import assert_steps



dis = distrindution
class TestAllocateOrders():
    """
    分配订单流程
    """

    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','get_query_order_data1')])
    def test_get_query_order_data(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.get_query_order_data(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','disibute_Orders')])
    def test_disibute_Orders(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.disibute_Orders(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

if __name__ == '__main__':
    pytest.main(['-s',r'./test_Allocate_orders.py'])