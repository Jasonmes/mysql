# """
# Python操作MySQL步骤
#    1. 通过Connection创建连接
#    2. 通过Connection对象创建游标
#    3. 通过游标执行sql语句(命令)
#    4. 通过游标获取结果集
#    5. 依据业务处理结果数据
#    6. 关闭游标
#    7. 关闭连接
# """
# import pymysql
#
#
# def main():
#     # 1. 通过Connection创建连接
#     """
#      host=None,
#      user=None,
#      password="",
#      database=None,
#      port=0,
#      charset=''
#     """
#     conn = pymysql.connect(host="localhost",
#                            user="root",
#                            password="ZHISHAO8@gezifu",
#                            database="JingDong",
#                            port=3306,
#                            charset='utf8')
#
#     # 2. 通过Connection对象创建游标
#     cs1 = conn.cursor()
#
#     # 3.  通过游标执行sql语句(命令)
#     sql = "select * from goods"
#     cs1.execute(sql)
#
#     # 4. 通过游标获取结果集
#     result = cs1.fetchall()
#
#     # 5. 依据业务处理结果数据
#     for item in result:
#         print(item)
#
#     # 6. 关闭游标
#     cs1.close()
#
#     # 7. 关闭连接
#     conn.close()
#
#
# if __name__ == '__main__':
#     main()  #alt+enter 快速修复

# 第一遍
# import pymysql
#
#
# def main():
#     # 1建立连接
#     conn = pymysql.connect(host='localhost',
#                            user='root',
#                            password='ZHISHAO8@gezifu',
#                            database='JingDong',
#                            port=3306,
#                            charset='utf8')
#     # 获取游标
#     cs1 = conn.cursor()
#     # 游标执sql语句
#     cs1.execute('select * from goods')
#     # 获取结果
#     result = cs1.fetchall()
#
#     # 遍历结果
#     for item in result:
#         print(item)
#
#     cs1.close()
#     conn.close()
#
#
# if __name__ == "__main__":
#     main()

# 第二遍
# import pymysql
#
#
# def main():
#     conn = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', database='JingDong', port=3306,
#                            charset='utf8')
#     cs1 = conn.cursor()
#     cs1.execute('select * from goods')
#     for item in cs1.fetchall():
#         print(item)
#     cs1.close()
#     conn.close()
#
#
# if __name__ == "__main__":
#     main()

# 第三遍
# import pymysql
#
# connnet_sql = pymysql.connect(host='localhost',
#                               user='root',
#                               password='ZHISHAO8@gezifu',
#                               database='JingDong',
#                               port=3306,
#                               charset='utf8')
# sql_cur = connnet_sql.cursor()
# sql_cur.execute('select * from goods')
# result_sql = sql_cur.fetchall()
# for item in result_sql:
#     print(item)
# sql_cur.close()
# connnet_sql.close()


# 第四遍
# import pymysql
#
# con_sql = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', port=3306, database='JingDong',charset='utf8')
# cur_sql = con_sql.cursor()
# cur_sql.execute('select * from goods')
# result_back = cur_sql.fetchall()
# for item in result_back:
# 	print(item)
# cur_sql.close()
# con_sql.close()

# 第五遍
import pymysql

con_sqkl = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu',port=3306,database='JingDong',charset='utf8')
cur_sql = con_sqkl.cursor()
cur_sql.execute('select * from goods')
back_info = cur_sql.fetchall()
for item in back_info:
	print(item)
cur_sql.close()
con_sqkl.close()