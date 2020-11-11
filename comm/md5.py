# coding=utf-8
# author:yundanni
# create_time:2020/11/2 17:00
import datetime
import hashlib
import time
import json
timestamp = int(time.time())
from util.rsa import Decript
# 定义公共参数
'''
auth_session=''
dvc_id='8b9f03dc8ad471d611d8a648afe0530b'
client_type='2'
# message={"mobile":"17310853906","password":"lz123456","country_code":"0086"}
message={'mobile': '17310853906', 'password': 'lz123456', 'country_code': '0086'}

params=Decript().rsa(message)
app_id='zhixing'
version='2.5.0'
timestamp = int(time.time())
print (timestamp)
api_key='MIA_XIAOHUAN_ANDROID'
params=Decript().rsa(message)
'''

class SignatureAndVerification(object):
    """MD5签名和验签"""
    # @classmethod
    def data_processing(self, data):
        """
        :param data: 需要签名的数据，字典类型
        :return: 处理后的字符串，格式为：参数名称=参数值，并用&连接
        """

        dataList = []
        for key in sorted(data):
            dataList.append("%s=%s" % (key, data[key]))
        return "&".join(dataList).strip()
        # print ("拼接api_key之前的字符串&".join(dataList).strip())

    # @classmethod
    def md5_sign(self, data, api_key):
        """
        MD5签名
        :param api_key: MD5签名需要的字符串
        :return: 签名后的字符串sign
        """

        data = self.data_processing(data) +'&key='+api_key.strip()
        # print (data)
        md5 = hashlib.md5()
        md5.update(data.encode(encoding='UTF-8'))
        return str.upper(md5.hexdigest())
        # print ("MD5加密后的字符串:"+ str.upper(md5.hexdigest()))

# a=SignatureAndVerification()
# data={"auth_session":"","dvc_id":dvc_id,"client_type":client_type,"params":params,"app_id":app_id,"version":version,"timestamp":timestamp}
# SignatureAndVerification().md5_sign(data, api_key)


