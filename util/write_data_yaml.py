# coding=utf-8
# author:yundanni
# create_time:2020/11/11 15:08
import os
import yaml
import sys
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]#将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
sys.path.append(BASE_PATH)
sys.path.append(UTILS_PATH)
DATA_PATH = os.path.join(BASE_PATH, r'data')
DATA_FILE = os.path.join(BASE_PATH, r'data\data.yaml')
data_config = {
                'api_path': {
                    "login_path":"/unioncenter/loginByPass/",
                    "Params":"/crontab/pushCron/push_live_info/220110452",
                    "index_path":"/unioncenter/index",
                    "live_detail":"/liveBroadcast/liveDetail"
                             },

                'user':
                    {'user1':
                         {
                        "mobile": "17310853906",
                        "password": "lz123456",
                        "country_code": "0086"}
                    },

                'host':'https://api.iyuansong.com',

                'data':{
                    'dvc_id':'8b9f03dc8ad471d611d8a648afe0530b',
                    'client_type':'2',
                    'app_id':'zhixing',
                    'version':'2.5.0'
                },


                'live_detail_data':{
                    "live_id":"6"
                }
}



# print (type(db_config['database']))
# print (data_config['api_path']['login_path'])
# print (data_config['user']['user2']['mobile'])





# 写入到yaml文件
# if DATA_FILE exist:
#
with open(DATA_FILE, "w", encoding="utf-8") as f:
    # yaml.dump(desired_caps, f)
    yaml.dump(data_config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)