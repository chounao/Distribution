import pytest
from api.distrinDution_api import distrindution
from common.assert_tools import assert_steps



dis = distrindution
class TestQueryTasksOrders():
    """
    同步订单流程
    """


    @pytest.mark.parametrize('yaml_path,case_name', [('distrindution_path', 'query_Lates_SyncTask01_orders')])
    def test_query_Lates_SyncTask01(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.query_Lates_SyncTask01_orders(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

    @pytest.mark.parametrize('yaml_path,case_name', [('distrindution_path', 'query_Lates_SyncTask2_orders')])
    def test_query_Lates_SyncTask2(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.query_Lates_SyncTask2_orders(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

    @pytest.mark.parametrize('yaml_path,case_name', [('distrindution_path', 'save_Sync_Task_orders')])
    def test_save_Sync_Task(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.save_Sync_Task_orders(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

    @pytest.mark.parametrize('yaml_path,case_name', [('distrindution_path', 'query_Sync_Task_Progress_orders')])
    def test_query_Sync_Task_Progress(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.query_Sync_Task_Progress_orders(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

if __name__ == '__main__':
    pytest.main(['-s',r'./test_query_order_Task.py'])