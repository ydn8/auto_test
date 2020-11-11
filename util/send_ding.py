# coding=utf-8
# author:yundanni
# create_time:2020/11/10 18:28
import requests
import time
import hashlib
import hmac
import base64
import re

def SendMessage(text):
    #https://oapi.dingtalk.com/robot/send?access_token=c3e0a68e0c9199e183dcc05369fba9f89368f9db2c52e120e8f5a809af5e1807

    # secret：密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的字符串，例如：SECxxxxxxxx
    secret = 'SEC96830f76cc543847c7b74a8a1e189a30da0a6f9ea28da532b8ec707d234ad9f9'

    # access_token：创建完钉钉机器人之后会自动生成，例如：access_tokenxxxx
    access_token = 'c3e0a68e0c9199e183dcc05369fba9f89368f9db2c52e120e8f5a809af5e1807'
    # timestamp：当前时间戳，单位是毫秒，与请求调用时间误差不能超过1小时
    timestamp = int(round(time.time() * 1000))

    # 加密，获取sign和timestamp
    data = (str(timestamp) + '\n' + secret).encode('utf-8')
    secret = secret.encode('utf-8')
    signature = base64.b64encode(hmac.new(secret, data, digestmod=hashlib.sha256).digest())
    reg = re.compile(r"'(.*)'")
    signature = str(re.findall(reg,str(signature))[0])

    # 发送信息
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&sign=%s&timestamp=%s' % (access_token,signature,timestamp)
    # print (url)
    headers = {"Content-Type": "application/json ;charset=utf-8 "}
    message={
            "msgtype":"text",
            "text":{"content":text},
            "at":{"isAtAll":False}
             }
    try:
        response = requests.post(url, headers = headers, json = message, timeout = (3,60))
        print(response)
        response_msg = str(response.status_code) + ' ' + str(response.content)
        print(response_msg)
    except Exception as error_msg:
        print('error_msg==='+str(error_msg))
        response_msg = error_msg

    return response_msg

if __name__ == "__main__":
    # msg = {"msgtype":"text","text":{"content":"测试"},"at":{"isAtAll":False}}
    # print (type(msg))
    SendMessage("200")