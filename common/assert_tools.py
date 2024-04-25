from common.yaml_tools import get_assert_data
def assert_steps(yaml_path,case_name,res):
    """

    :param yaml_path: ini文件case路径的key
    :param case_name: yaml文件case的name
    :param res: 发送请求的结果
    :return:
    """
    rcode, scode = get_assert_data(yaml_path,case_name)
    assert rcode == res.json().get("rcode")
    assert scode == res.json().get("scode")
