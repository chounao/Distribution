import pytest
from common.assert_tools import assert_steps
from api.login_api import login


class TestLogin:
    @pytest.mark.parametrize('yaml_path,case_name,url',[('login_path', 'Test Login_Case', 'Login_URL')])
    def test_login(self,yaml_path,case_name,url):

        result = login.fhd_login()
        assert_steps(yaml_path, case_name, result)


if __name__ == '__main__':
    pytest.main(['-s',r'./test_login.py'])