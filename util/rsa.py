# coding=utf-8
# author:yundanni
# create_time:2020/11/2 17:03
# coding:utf-8
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcsl_v1_5
import base64
import json


class Decript:

    def rsa(self, message):
        self.public_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD3KBsaV5nokgj+a8QXIoSFtuJN
Sv7c+rK/6EifG2ztg4mnHNDABkD7YbkrVRy0brS8804rLOzlhS5w2dJjEfWlLcCQ
i7relUDK3Sbt2RpJWhp7phblT/NHsH6Ai3ubzHpNiWg2q7JJl502MW24AjtVzCb4
etn8+AExxCzYoDbPvwIDAQAB
-----END PUBLIC KEY-----
'''
        self.msg = json.dumps(message)
        self.rsakey = RSA.importKey(self.public_key)
        self.cipher = Cipher_pkcsl_v1_5.new(self.rsakey)
        self.cipher_text = base64.b64encode(self.cipher.encrypt(self.msg.encode())).decode()
        return((self.cipher_text))

# my_data=my_data()
# a.data_processing(data)
# print (a)
# a.md5_verify(data,api_key)

#message={"mobile":"17310853906","password":"lz123456","country_code":"0086"}

# auth_session=''
# dvc_id='8b9f03dc8ad471d611d8a648afe0530b'
# client_type='2'
# params='EWFRgsZD3BMHCpFR/1AZ/bXwd3Va+y+tqrTysn8yYTLIiDjVrxTUlb/nRggrJ6x0aFxuC+v8RfaYqexExZPTBn85+q99y8aHlMz5r0G4Rtl4z8/jLYZ6vF1h2wiNf03TdwqLc7YmEQ95\
# WLgYUHjt7UYGj2W2ycj'
# app_id='zhixing'
# version='2.5.0'
# timestamp='1604296500'
#
# a=Decript()
# cipher_text=a.rsa(message)
