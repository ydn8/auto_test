# coding=utf-8
# author:yundanni
# create_time:2020/11/6 18:06
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
对yaml格式的配置文件的操作
"""

import yaml
import os
import sys
# curPath = os.path.dirname(os.path.realpath(__file__))
# path=curPath
# print (curPath)
# print (os.path.abspath(__file__))
# print (os.path.dirname(os.path.abspath(__file__)))

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]#将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
# print ('base_path= '+BASE_PATH)
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
sys.path.append(BASE_PATH)
sys.path.append(UTILS_PATH)
DATA_PATH = os.path.join(BASE_PATH, r'data')
DATA_FILE = os.path.join(BASE_PATH, r'data\data2.yaml')
DB_FILE = os.path.join(BASE_PATH, r'config\db_config.yaml')


# DATA_PATH = os.path.join(BASE_PATH, 'data')
# REPORT_PATH = os.path.join(BASE_PATH, 'report')
# INTERFACE_PATH = os.path.join(BASE_PATH, 'interface')



class YamlHandle():
    def __init__(self, yamlf):

        if os.path.exists(yamlf):
            self.yamlf = yamlf
            self.cfg = open(self.yamlf, 'r', encoding='utf-8')

        else:
            raise FileNotFoundError('文件不存在！')

    """
        api_path:
          login_path: /unioncenter/loginByPass/
        user:
        - user1:
            country_code: 0086
            mobile: '17310853906'
            password: lz123456
          user2:
            country_code: 0086
            mobile: '18612162828'
            password: zhaoru1987

    """
    def get_value(self, *keys):
        """
        @param keys:yaml文件中的key值，可多层，['password_input','dec']或者['password_input']
        @return: 返回字典中value值
        """

        try:
            data_dict = yaml.load(self.cfg, Loader=yaml.FullLoader)  # 用load方法转字典
            # print (data_dict)
            if not keys:
                return data_dict
            else:
                for key in keys:
                    tmp = data_dict.get(key)
                    if tmp is not None:
                        data_dict = tmp
                return data_dict
        except:
            print("值不存在")

    @property
    def get_yaml_data(self):
        self.data_dict = yaml.load(self.cfg, Loader=yaml.FullLoader)
        return (self.data_dict)
    # def __del__(self):
    #     try:
    #         self.f.close()
    #     except:
    #         print("文件操作符关闭失败")


if __name__ == '__main__':
    yh = YamlHandle(DB_FILE)
    # print(yh.get_yaml_data['host'])

    # print(yh.get_value('api_path').get('login_path')) #读取字典
    #print(yh.get_value('user')[0]['user1'])  #读取列表套字典