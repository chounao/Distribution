import pytest
from api.distrinDution_api import distrindution
from common.assert_tools import assert_steps


dis = distrindution
class TestQuery():

    #厂家代发未分配，已分配未发货，已分配已发货
    @pytest.mark.parametrize('yaml_path,case_name',
                             [('distrindution_path','get_query_order_data1'),
                             ('distrindution_path','get_query_order_data2'),
                            ('distrindution_path','get_query_order_data3')])
    def test_get_query_order_data(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.get_query_order_data(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','query_DistributionItem')])
    def test_query_DistributionItem(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.query_DistributionItem(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

    #厂家代发分配设置
    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','get_configuration')])
    def test_get_configuration(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.get_configuration(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)


    # @pytest.mark.parametrize('yaml_path,case_name', [('distrindution_path', 'save_configuration')])
    # def test_save_configuration(self, yaml_path, case_name, get_MySingleton_Data):
    #     set_url = globals().get('url')
    #     result = dis.get_configuration(yaml_path, case_name, set_url)
    #     assert_steps(yaml_path, case_name, result)


    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','query_items_data')])
    def test_query_items_data(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.query_items_data(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)

    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','query_sku_data')])
    def test_query_skus_data(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.query_sku_data(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)








if __name__ == '__main__':
    pytest.main(['-s',r'./test_query.py'])