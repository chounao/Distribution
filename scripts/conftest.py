import pytest
from common.set_up_steps import steps
from common.SingLeton_tools import MySingleton
from api.login_api import login
from scripts.test_login import TestLogin
@pytest.fixture(scope='session',autouse=True)
#登陆主要获取token并且更新所有yaml内token
def LOGGIN():
    login.fhd_login()




@pytest.fixture(scope='class',autouse=True)
def updata(platform='抖音'):
     steps(platform)

@pytest.fixture
def get_MySingleton_Data():
    url = MySingleton.get_data('url')
    # print(url)
    return url



