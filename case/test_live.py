# coding=utf-8
# author:yundanni
# create_time:2020/11/10 17:50
import json
from log.logger_handler import LoggerHandler
import os
from comm.form_data import Post_data
from util.request_method import method
from util.send_ding import SendMessage

log_name=os.path.dirname(os.path.abspath(__file__))
log_file='zhixing_log_file'
mylogger = LoggerHandler(log_file,log_name).get_log()
case_name="live_detail"
class Testlive:
    def __init__(self):
        #定义接口请求url和post data
        self.post_url=Post_data().post_url(case_name)
        self.post_data=Post_data().post_data(case_name)

    def test_live(self):
        mylogger.info("测试用例%s开始执行" % case_name)
        self.res = method().send_post(self.post_url, self.post_data)
        self.jres=json.dumps(self.res.json(), sort_keys=True, indent=4, separators=(',', ':'))
        print(self.jres)

        # SendMessage(self.res.status_code)
        # self.assertEqual(self.jres['status'],200,msg='测试失败')
        print(u"*" * 80)

Testlive().test_live()
