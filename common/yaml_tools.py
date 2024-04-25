from common.read_tools import ReadFileData
import os
import yaml
from common.read_config import Read_Config

os_path = os.path.dirname(os.getcwd())
def get_yaml_path(yaml_path):
    """

    :param yaml_path: ini文件case路径的key
    :return:
    """
    #先把公用方法调用一次
    read = Read_Config()
    case_path = read.get_config_yamlpath(yaml_path)
    return case_path

#获取yaml数据
def get_yaml_case_tools(yaml_path):
    """

    :param yaml_path:ini文件case路径的key
    :return:yaml对应的数据
    """
    case_path = get_yaml_path(yaml_path)
    file_path = os_path+case_path
    get = ReadFileData()
    yaml_data = get.load_yaml(file_path)
    #print(yaml_data,"data")
    return yaml_data
#写入yaml数据
def write_yaml(yaml_path,data):
    """
    :param yaml_path: ini文件case路径的key不过这里是更新的文件key
    :param data:
    :return:
    """
    #文件路径
    case_path = get_yaml_path(yaml_path)
    file_path = os_path+case_path
    with open(file_path,'w',encoding='utf-8') as file:
        yaml.dump(data, file)
#更新yaml数据
def updata_case(yaml_path,key,value):
    """
    :param yaml_path: ini文件case路径的key不过这里是更新的文件key
    :param key: 参数对应的key
    :param value: 参数对应的valu
    :return:
    """
    yaml_data = get_yaml_case_tools(yaml_path)
    for case_test in yaml_data:
        params = case_test['request']['params']
        if key in params:
            params[key] = value
    write_yaml(yaml_path,yaml_data)



def updata_case_for_casename(yaml_path,casename,key,value):
    """
    :param yaml_path: ini文件case路径的key不过这里是更新的文件key
    :param key: 参数对应的key
    :param value: 参数对应的valu
    :param casename: yaml文件对应的casename
    :return:
    """
    yaml_data = get_yaml_case_tools(yaml_path)
    for case_test in yaml_data:
        if casename == case_test['name']:
            params = case_test['request']['params']
            if key in params:
                params[key] = value
    write_yaml(yaml_path, yaml_data)

#根据用例名字获取对应数据
def get_request_data(yaml_path,case_name):
    """

    :param yaml_path: ini文件case路径的key
    :param case_name: yaml文件case的name
    :return:
    """
    yaml_data = get_yaml_case_tools(yaml_path)
    for test_case in yaml_data:
        if test_case['name'] == case_name:
        #获取 请求参数
            yaml_request_data = test_case['request']
            method = yaml_request_data['method']
            path = yaml_request_data['path']
            params = yaml_request_data['params']
            headers = yaml_request_data['headers']
            #print(method,path,params,headers)

            return method,path,params,headers

def get_assert_data(yaml_path,case_name):
    #获取断言
    """

    :param yaml_path: ini文件case路径的key
    :param case_name: yaml文件case的name
    :return:
    """
    yaml_data = get_yaml_case_tools(yaml_path)
    for test_case in yaml_data:
        if test_case['name'] == case_name:
            assert_data = test_case['assert']
            rcode = assert_data['rcode']
            scode = assert_data['scode']
            return rcode, scode







if __name__ == '__main__':
    #updata_case("platform_path",'token','20')
    # updata_param("/run_case_yaml/shop_data/case_shop.yaml")
    get_assert_data('platform_path','Test Get marsId And marsCode')
