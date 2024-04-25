import yaml
import json
from configparser import ConfigParser

class MyconfigParser(ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.__init__(self,defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():
    def __init__(self):
        pass
    def load_yaml(self,file_path):
        with open(file_path,'r',encoding='utf-8')as f:
            data = yaml.safe_load(f)
            return data

    def load_json(self,file_path):
        with open(file_path,'r',encoding='utf-8')as f:
            data = json.load(f)
            return data

    def load_ini(self,file_path):
        config = MyconfigParser()
        config.read(file_path,encoding='utf-8')
        data = dict(config._sections)
        return data




