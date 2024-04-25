import pytest
from api.distrinDution_api import distrindution
from common.assert_tools import assert_steps





dis = distrindution
class TestUnbindingManufacturer():
    """
    解绑厂家
    """

    @pytest.mark.parametrize('yaml_path,case_name', [('distrindution_path', 'check_Distribution_Order')])
    def test_check_Distribution_Order(self, yaml_path, case_name, get_MySingleton_Data):
        result = dis.check_Distribution_Order(yaml_path, case_name, get_MySingleton_Data)
        assert_steps(yaml_path, case_name, result)