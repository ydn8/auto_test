# coding=utf-8
# author:yundanni
# create_time:2020/11/9 18:11
# encoding: utf-8
import sys
import os,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sys.path.append("\\case")#这样引用必须在文件夹中新建__init__文件
result = "..\\report\\"
sys.path.append('..\\log')
sys.path.append('..\\config')
from read_config import TestReadConfigFile
from logg import Log
mylogger =Log(logger_name='mail').get_log()
class SendMail():
    global subject,mail_to_i,mail_from_i,mail_to_text
    readcf=TestReadConfigFile()
    subject=readcf.get_value()[0]
    mail_to_i=readcf.get_value()[1]
    mail_from_i=readcf.get_value()[2]
    mail_to_text=readcf.get_value()[3]

    def sendmail(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        tdresult = result + day
        # 读取文件
        filename = tdresult + "\\"
        # print filename

        lists = os.listdir(filename)
        lists.sort(
            key=lambda fn: os.path.getmtime(filename + "\\" + fn) if not os.path.isdir(filename + "\\" + fn) else 0)
        print (u'最新测试生成的报告:' + lists[-1])
        file_new = os.path.join(filename, lists[-1])
        mylogger.info(u'最新文件路径为是：%s'%(file_new))
        # 发送邮件
        # 构建邮件
        msg = MIMEMultipart()
        txt = '<html><body>selenium自动化测试报告！ </br>测试组：贠丹妮 </br></body></html>'
        att1 = MIMEText(txt, 'html', 'utf-8')
        msg.attach(att1)
        # 构建附件
        att2 = MIMEText(open(file_new, "rb").read(), "base64", "utf-8")
        att2["Content-Type"] = 'application/octet-stream'
        att2[
            "Content-Disposition"] = 'attachment; filename="interface_test_report.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(att2)
        # 构建邮件发送区域文字
        msg['to'] = mail_to_text
        msg['from'] = mail_from_i
        msg['Subject'] = subject
        msg['date'] = time.strftime('%Y/%m/%d %H:%M:%S')
        # 设置发送地址
        smtp = smtplib.SMTP()
        mail_from = mail_from_i
        mail_to = mail_to_i
        # 连接服务器
        try:
            smtp.connect('smtp.jiuyescm.com')
            smtp.login('yundanni@jiuyescm.com', '187927YDN@@')
            smtp.sendmail(mail_from, mail_to, msg.as_string())
            smtp.quit()
            mylogger.info(u'邮件发送成功！')
        except:
            mylogger.info(u'邮件发送失败！')

if __name__=='__main__':
    mail=SendMail()
    mail.sendmail()







