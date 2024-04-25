import requests
from common.read_config import Read_Config
from common.yaml_tools import get_request_data


def requests_data(yaml_path,case_name,config_url):
    """
    获取对应的参数发送request请求
    :param yaml_path: cese执行的路径，这里是读取ini配置写对应的key
    :param case_name:yaml对应的casename分别执行哪条用例
    :param config_url:url的路径，这里也是读Ini配置的对应的Key(如果url唯一可以不用)
    :return:
    """
    read = Read_Config()
    url = read.get_config_url(config_url)
    method, path, params, headers = get_request_data(yaml_path,case_name)
    request_url = url + path
    print("发送请求的参数",method, path, params, headers,request_url)
    s = requests.session()
    try:
        if method == "get":
            result = s.get(request_url,params,headers)
        elif method == 'post':
            if "application/json" in headers:
                result = s.post(request_url,params,headers)
            else:
                result = s.post(request_url,params,headers)
        else:
            print("其他请求")
        return result
    except Exception as e:
        print("http请求报错：%s" % e)






