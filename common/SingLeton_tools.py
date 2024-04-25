

class MySingleton:
    """
    保证对象全局唯一
    声明一个数据对象
    进行存储和获取操作
    """
    _instance = None
    _data = {}
    @staticmethod
    def get_instance():
        if MySingleton._instance is None:
            MySingleton()
        return MySingleton._instance
    def __init__(self):
        if MySingleton._instance is not None:
            raise Exception('This class is a singleton')
        else:
            MySingleton._instance = self
    @staticmethod
    def set_data(key,value):
        MySingleton._data[key] = value
    @staticmethod
    def get_data(key):
        return MySingleton._data.get(key)

