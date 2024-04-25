# from common.read_tools import ReadFileData
# import os
# def get_yaml_case_tools(yaml_path):
#     read = ReadFileData()
#     file_path = os.path.dirname(os.getcwd()) +yaml_path
#     yaml_data = read.load_yaml(file_path)
#     # print(yaml_data)
#     return yaml_data
#
#
#
#
# def get_request_data(yaml_path,case_name):
#     yaml_data = get_yaml_case_tools(yaml_path)
#     for test_case in yaml_data:
#         if test_case['name'] == case_name:
#             # print(test_case['name'])
#         #获取 请求参数
#             yaml_request_data = test_case['request']
#             method = yaml_request_data['method']
#             path = yaml_request_data['path']
#             params = yaml_request_data['params']
#             headers = yaml_request_data['headers']
#             # print(method,path,params,headers)
#
#             return method,path,params,headers
#
# def get_assert_data(yaml_path):
#     #获取断言
#     assert_data = get_yaml_case_tools(yaml_path)[0]['assert']
#     rcode = assert_data['rcode']
#     scode = assert_data['rcode']
#
#     return rcode,scode
#
# def updata_params(yaml_path,case_name,key:list,value:list):
#     #更新参数
#     method,path,params,headers= get_request_data(yaml_path,case_name)
#     params_dit = dict(params)
#     params_dit = {**params_dit, **{k: v for k, v in zip(key, value)}}
#     return method,path,params_dit,headers
#
# # def updata_param(yaml_path):
# #     yaml_data = get_yaml_case_tools(yaml_path)
# #     for i in yaml_data:
# #         print(i)
# #
#
#
#
#
# if __name__ == '__main__':
#     get_request_data("/run_case_yaml\login\case_login.yaml")
#     # get_assert_data("/run_case_yaml\login\case_login.yaml")
#     # get_request_data("/run_case_yaml/shop_data/case_shop.yaml","Test Get marsId And marsCode")
#     #updata_params("/run_case_yaml\login\case_login.yaml",['username','userppp','uesr333'],['111','222','333'])
#     # updata_param("/run_case_yaml/shop_data/case_shop.yaml")