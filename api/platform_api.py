from common.request_tools import requests_data
from common.read_config import Read_Config
from common.yaml_tools import updata_case

def set_platform(platform_path):
    #获取平台对应参数
    read = Read_Config()
    platform = read.get_config_platfrom(platform_path)
    return platform

def set_phone(phone):
    """

    :param phone: ini文件电话的key
    :return:
    """
    read = Read_Config()
    num = read.get_phoneNumber(phone)
    return num



def get_shop_data(platform_path):
    """
    只是根据平台信息获取对应的内容
    :param platform_path: ini文件case路径的key
    :return: shopid ,shopname()
    """
    platform=set_platform(platform_path)
    # 发送请求操作这里直接用case路径地址key，casename,和url路径的key
    data = requests_data('platform_path','Test Get ShoId And Url','Commonapi_URL')
    params_data = data.json()['data']
    data_list = []
    #根据平台判断相关数据抖音的和其他平台不一致
    for i in params_data:
        if platform == i['platformType']:
            data_dict = {}
            shopid = i['platformKey']
            name = i['name']
            data_dict['name'] = name
            data_dict['shopid'] = shopid
            data_list.append(data_dict)

    updata_case('platform_path','platform',platform)
    updata_case('distrindution_path', 'platform', platform)

    return data_list


def get_getDistributorList(platform_path):
    '''
    根据平台拿到的参数再取出自己绑定手机号的相关参数（上面返回的值有很多其他厂商的信息）
    :param platform_path: ini文件case路径的key
    :return: marsId,marscode
    '''
    phone_number = set_phone('phone_number')
    try:
        for i in get_shop_data(platform_path):
            #因为返回多个商家信息多次更新对应的case内容后去发送请求然后去判断对应的厂商是否在
            updata_case('platform_path','shopId',i['shopid'])
            # 发送请求操作这里直接用case路径地址key，casename,和url路径的key
            data = requests_data('platform_path','Test Get marsId And marsCode','Commonapi_URL')
            params_data = data.json()['data']['list']

            data_list = []
            for n in params_data:
                # 判断当使用的手机号和ini文件手机号一致
                if phone_number == n['factoryAccount']:
                    data_ditc={}
                    marsId = n['marsId']
                    marsCode = n['marsCode']
                    data_ditc['marsId'] = marsId
                    data_ditc['marsCode'] = marsCode
                    data_ditc['shopid'] = i['shopid']
                    data_ditc['name'] = i['name']
                    data_list.append(data_ditc)
                    print("{}{}绑定手机:{}".format(platform_path, marsId,phone_number))
            return data_list
    except:
        print("{}没有绑定手机:{}".format(platform_path, phone_number))


def update_case(platform_path):
    # 判断是否绑定：没有绑定参数是空的
    # 不为空后更新测试用例内容
    data_list = get_getDistributorList(platform_path)
    print(data_list)
    if data_list[0] == None:
        print("看看数据为{}".format(data_list[0]))
    else:
        updata_case('distrindution_path', 'marsId', data_list[0]['marsId'])
        updata_case('distrindution_path', 'marsCode', data_list[0]['marsCode'])
        updata_case('distrindution_path', 'shopId', data_list[0]['shopid'])
        # shopToken = "[{'shopId':'{}','shopName':'{}'}]".format(data_list[0]['shopid'], data_list[0]['name'])
        shopToken = [{'shopId': data_list[0]['shopid'], 'shopName': data_list[0]['name']}]
        updata_case('distrindution_path', 'shopToken', str(shopToken))

if __name__ == '__main__':

    updata_case('视频号')
