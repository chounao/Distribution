import pytest
from api.distrinDution_api import distrindution
from common.assert_tools import assert_steps



dis = distrindution
class TestgetLink():
    """
    生成厂家绑定链接
    """
    @pytest.mark.parametrize('yaml_path,case_name',[('distrindution_path','get_Manufacturer_Link')])
    def test_get_Manufacturer_Link(self,yaml_path,case_name,get_MySingleton_Data):
        result = dis.get_Manufacturer_Link(yaml_path,case_name,get_MySingleton_Data)
        assert_steps(yaml_path,case_name,result)



if __name__ == '__main__':
    pytest.main(['-s',r'./test_Manufacturer_link.py'])