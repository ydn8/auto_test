# coding=utf-8
# author:yundanni
# create_time:2020/11/11 11:40
import os
import pymysql
from log.logger_handler import LoggerHandler
import sys
from config.get_config import Config

log_name=os.path.dirname(os.path.abspath(__file__))
log_file='dab_log_file'
mylogger = LoggerHandler(log_file,log_name).get_log()
case_name="db"

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]#将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
# UTILS_PATH = os.path.join(BASE_PATH, 'utils')
# sys.path.append(BASE_PATH)
# sys.path.append(UTILS_PATH)
# DATA_PATH = os.path.join(BASE_PATH, r'data')
# DATA_FILE = os.path.join(BASE_PATH, r'data\data2.yaml')
DB_FILE=os.path.join(BASE_PATH, r'config\db_config.yaml')
db_file=Config(DB_FILE).


class DBHelper():
    # 构造函数,初始化数据库连接
    def __init__(self,sql,params=None):
        self.sql = sql
        self.params = params
        self.conn = None
        self.cur = None

    def connectiondatabase(self):
        db_config=
        print(db_config['host'],db_config['username'],db_config['password'],db_config['database'],db_config['charset'])
        try:
            self.conn = pymysql.connect(db_config['host'],db_config['username'],
                                    db_config['password'],db_config['database'],charset=db_config['charset'])
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True



    # 关闭数据库
    def closedatabase(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self):
        self.connectiondatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(self.sql,self.params)
                self.conn.commit()
        except:
            logger.error("execute failed: " + self.sql)
            logger.error("params: " + self.params)
            self.closedatabase()
            return False
        return True

    # 用来查询表数据
    def select(self):
        self.connectiondatabase()
        self.cur.execute(self.sql,self.params)
        result = self.cur.fetchall()
        print(result)
        return result
