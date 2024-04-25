from common.read_tools import ReadFileData
import os
class Read_Config():
    def __init__(self):
        pass
    def get_config(self):
        file_path = os.path.dirname(os.getcwd())+"/config.ini"
        read = ReadFileData()
        data = read.load_ini(file_path)
        return data
    def get_phoneNumber(self,phone_number):
        data = self.get_config()
        phone = data['DATA'][phone_number]
        return phone
    def get_config_url(self,config_url):
        data = self.get_config()
        url = data['URL'][config_url]
        return url

    def get_config_platfrom(self,config_platfrom):
        data = self.get_config()
        platfrom = data['Platform'][config_platfrom]
        return platfrom

    def get_config_yamlpath(self,config_yamlpath):
        data = self.get_config()
        yaml_path = data['YAMLPATH'][config_yamlpath]
        return yaml_path

if __name__ == '__main__':
    a = Read_Config()
    a.get_config_yamlpath('login_path')