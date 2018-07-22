# import pymysql
#
#
# # 1. 创建连接
# conn = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', port=3306, database='JingDong',charset='utf8')
#
# # 2. 取得游标
# cs1 = conn.cursor()
#
# # 3. 执行sql语句，实现增删改操作
# # 3.1 添加记录
# cs1.execute("insert into goods value(1,'applewatch','穿戴设备','苹果','3444',default,default)")
# conn.commit()  # 假如对数据库进行增删改，则需要提交
#
# # 3.2 更新记录
# # affect_rows = cs1.execute("update goods set name='手环' WHERE id=9")
# # conn.commit()  # 假如对数据库进行增删改，则需要提交
# #
# # if affect_rows == 1:
# #     print("修改成功")
# # else:
# #     print("修改失败")
#
# # 3.3 删除记录
# # affect_rows = cs1.execute("delete from goods where id=1")
# # print("影响的行数：", affect_rows)
# # conn.commit()  # 假如对数据库进行增删改，则需要提交
# #
# # if affect_rows==1:
# #     print("修改成功")
# # else:
# #     print("修改失败")
# #
# # # 4. 关闭游标，连接
# # cs1.close()
# # conn.close()


# 第一遍
# import pymysql
# # 链接mysql
# sql_con = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', database='JingDong', port=3306, charset='utf8')
# # 创建游标
# cur_sql = sql_con.cursor()
# # 使用游标来操作mysql
# # 添加记录
# excute一定要用双引号
# #cur_sql.execute("insert into goods value(0,'EP21','耳机','魅族','168',default,default)")
# #sql_con.commit()
# # 更行修改
# #cur_sql.execute("update goods set cate_name='穿戴设备' where id=9")
# #sql_con.commit()
# ## 删
# #cur_sql.execute('delete from goods where id=9')
# #sql_con.commit()
#
# #cur_sql.execute('select * from goods')
#
# cur_sql.close()
# sql_con.close()

# 第二遍

import pymysql
#连接
connected = pymysql.connect(host='localhost', port=3306, user='root', password='ZHISHAO8@gezifu', database='JingDong',charset='utf8')
#游标
cur = connected.cursor()
#游标执行命令
#插入信息
#cur.execute("insert into goods value(0,'series3','穿戴设备','苹果','3333',default,default)")
#connected.commit()
#
##更新信息
#cur.execute("update goods set cate_name='手环小米' where id=7")
#connected.commit()

#删除
cur.execute("delete from goods")
connected.commit()

cur.close()
connected.close()
