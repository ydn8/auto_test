# coding=utf-8
# author:yundanni
# create_time:2020/11/6 18:09
import os


'''***获取当前目录***'''
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))

'''***获取上级目录***'''
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

'''***获取上上级目录***'''
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))