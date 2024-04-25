from common.request_tools import requests_data
from common.yaml_tools import updata_case



# class login:
#     @classmethod
#     def fhd_login(csl,yaml_path, case_name,config_url):
#         result = requests_data(yaml_path, case_name,config_url)
#         for i in dict(result.headers).get('Set-Cookie').split(','):
#             if 'fhd_token=%' in i:
#                 token = i.split(';')[0][11:]
#                 print(token)
#                 updata_case('platform_path', 'token', token)  # 更新token.
#                 updata_case('distrindution_path', 'token', token)
#         return result


class login:
    @classmethod
    def fhd_login(csl):
        result = requests_data('login_path', 'Test Login_Case', 'Login_URL')
        for i in dict(result.headers).get('Set-Cookie').split(','):
            if 'fhd_token=%' in i:
                token = i.split(';')[0][11:]
                print(token)
                updata_case('platform_path', 'token', token)  # 更新token.
                updata_case('distrindution_path', 'token', token)
        return result


