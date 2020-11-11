# coding=utf-8
# author:yundanni
# create_time:2020/11/2 18:16
# import requests
import json
import os
import sys
import time
from util.file_read import YamlHandle
from util.request_method import method,Decript
from comm.md5 import SignatureAndVerification
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]#将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
sys.path.append(BASE_PATH)
sys.path.append(UTILS_PATH)
DATA_PATH = os.path.join(BASE_PATH, r'data')
DATA_FILE = os.path.join(BASE_PATH, r'data\data.yaml')
DB_FILE=os.path.join(BASE_PATH, r'config\db_config.yaml')
data = YamlHandle(DATA_FILE).get_yaml_data
# print (data)
class Login:

    def __init__(self):
        #定义公共参数
        self.dvc_id = data["data"]["dvc_id"]
        # print (self.dvc_id )
        self.client_type = data["data"]["client_type"]
        self.app_id = data["data"]["app_id"]
        self.version = data["data"]["version"]
        timestamp = str(int(time.time()))
        self.app_key = 'MIA_XIAOHUAN_ANDROID'
        self.auth_session=''
        self.message=data["user"]["user1"]
        #获得rsa加密后的params
        self.params=Decript().rsa(self.message)
        self.login_url = str(data["host"] + data["api_path"]["login_path"])

        #获得sign
        self.data={'auth_session': self.auth_session, 'dvc_id': self.dvc_id, 'client_type': self.client_type,
            'params': self.params, 'app_id': self.app_id, 'version': self.version, 'timestamp': timestamp}
        self.sign=SignatureAndVerification().md5_sign(self.data,self.app_key)
        #拼接
        self.post_data={'auth_session': self.auth_session, 'dvc_id': self.dvc_id,'sign':self.sign, 'client_type': self.client_type,
            'params': self.params, 'app_id': self.app_id, 'version': self.version, 'timestamp': timestamp}

    def login(self):
        self.res=method().send_post(self.login_url,self.post_data)
        self.jres = json.dumps(self.res.json(), indent=1)
        # print (self.jres)
        self.auth_session=self.res.json().get('data').get('auth_session')
        # return self.jres
        return self.auth_session
        # print(self.auth_session)
        # print (self.jres)

    # def get_session(self):
    #     self.auth_session=self.res.json().get('data').get('auth_session')
    #     return (self.auth_session)
        # print (self.auth_session)
#同一类下的函数参数调用，要实例化
# a=Login()
# a.login()
# a.get_session()


#底下这种不行
# Login().login()
# Login().get_session()