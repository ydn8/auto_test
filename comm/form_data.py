# coding=utf-8
# author:yundanni
# create_time:2020/11/10 17:11
import json
import os
import sys
import time
from comm.login import Login
from comm.md5 import SignatureAndVerification
from util.file_read import YamlHandle
from util.rsa import Decript

timestamp = str(int(time.time()))
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]#将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
sys.path.append(BASE_PATH)
sys.path.append(UTILS_PATH)
DATA_PATH = os.path.join(BASE_PATH, r'data')
DATA_FILE = os.path.join(BASE_PATH, r'data\data.yaml')
DB_FILE=os.path.join(BASE_PATH, r'config\db_config.yaml')
data=YamlHandle(DATA_FILE).get_yaml_data

class Post_data:
    def __init__(self):
        #定义公共参数，接口传参这几个参数基本不变
        self.dvc_id = data["data"]["dvc_id"]
        # print (self.dvc_id )
        self.client_type = data["data"]["client_type"]
        self.app_id = data["data"]["app_id"]
        self.version = data["data"]["version"]
        timestamp = str(int(time.time()))
        self.app_key = 'MIA_XIAOHUAN_ANDROID'
        self.auth_session = Login().login()

    def post_url(self,path):
        #参数化获取请求url
        self.login_url = data["host"] + data["api_path"][path]
        return self.login_url



    def post_data(self,path):
        #获取业务参数
        #写yaml文档的时候，接口路径和这个接口的业务参数命名规则是：接口路径:**_path,接口对应的业务参数**_path_data
        self.mes=str(path+'_data')
        # print (self.mes)
        self.message = data[self.mes]
        #把业务参数rsa加密
        self.params=Decript().rsa(self.message)
        #准备拼接不带sign的参数，用于md5加密
        self.data = {'auth_session': self.auth_session, 'dvc_id': self.dvc_id, 'client_type': self.client_type,
                     'params': self.params, 'app_id': self.app_id, 'version': self.version, 'timestamp': timestamp}
        # print (self.data)
        self.sign = SignatureAndVerification().md5_sign(self.data, self.app_key)
        # # 拼接最终的接口post请求参数
        self.post_data = {'auth_session': self.auth_session, 'dvc_id': self.dvc_id, 'sign': self.sign,
                          'client_type': self.client_type,
                          'params': self.params, 'app_id': self.app_id, 'version': self.version, 'timestamp': timestamp}
        # print(json.dumps(self.post_data,sort_keys=True, indent=4, separators=(',', ':')))
        return self.post_data

a=Post_data()
a.post_data('live_detail')
a.post_url('live_detail')



