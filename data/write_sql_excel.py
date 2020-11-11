# coding=utf-8
# author:yundanni
# create_time:2020/11/11 11:06

"""
功能：将Excel数据导入到MySQL数据库   excel和该文件放在同一目录下
"""
import xlrd
import pymysql
from sqlalchemy.sql.functions import now

# from utils.common_util.pwd_util import admin_pwd_digest

book = xlrd.open_workbook(u"会员数据参考模板.xlsx")
sheet = book.sheet_by_name("Sheet1")

# 建立一个MySQL连接
conn = pymysql.connect(host="172.16.104.207", user="write_user", passwd="write_pwd", db="mia_plus_test", charset="utf8",port="3308")

# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
try:
    for row in range(1, sheet.nrows):
        phone = sheet.cell(row, 1).value  # （从0开始）1表示第二列
        if isinstance(phone, float):
            new_phone = str("{:.0f}".format(phone)).strip()
        else:
            new_phone = str(phone).strip()
        password = sheet.cell(row, 2).value
        sex = sheet.cell(row, 3).value
        status = sheet.cell(row, 4).value
        basics_nick_name = sheet.cell(row, 5).value
        company = sheet.cell(row, 6).value
        basics_sex = 0
        gmt_created = now()
        gmt_modified = now()
        query = "insert into qzx_user (phone, password, sex, basics_nick_name, basics_sex, " \
                "company, gmt_created, gmt_modified) values('%s','%s',%s,'%s','%s','%s',%s,%s)" \
                % (new_phone, password, sex, basics_nick_name, basics_sex,
                   company, gmt_created, gmt_modified)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    # 打印结果
    print
    ("Done! ")
    conn.close()
    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    print
    ("我刚导入了 " + columns + " 列 and " + rows + " 行数据到MySQL!")
except Exception as e:
    print
    e
    print
    ("导入出错！！！")
