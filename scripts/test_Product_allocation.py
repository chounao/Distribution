import pytest
from api.distrinDution_api import distrindution
from common.assert_tools import assert_steps





dis = distrindution
class TestAllocationProduct():
    """
    商品绑定厂家流程
    """


    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','query_DistributionItem')])
    def test_query_DistributionItem(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.query_DistributionItem(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)



    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','bind_DistributionItem_Factory')])
    def test_bind_DistributionItem_Factory(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.bind_DistributionItem_Factory(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)








if __name__ == '__main__':
    pytest.main(['-s',r'./test_Product_allocation.py'])