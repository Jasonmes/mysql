# import pymysql
#
#
# def main():
#     # 创建连接
#     conn = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', port=3306, database='JingDong', charset='utf8')
#
#     # 创建游标,默认获取的是元组游标，查询的结果是以元组的形式呈现的
#     cs1 = conn.cursor()   # ctrl+alt+v
#
#     sql = "select * from goods"
#     # 执行查询
#     affect_rows = cs1.execute(sql)
#     print("影响的行数:", affect_rows)
#
#     # 获取结果,抓取结果集中的一条数据，默认是从第一条开始
#     # 一条记录封装在元组中  --》(1, 'r510vc 15.6英寸笔记本', 1, 2, Decimal('3399.000'), b'\x01', b'\x00')
#     item = cs1.fetchone()
#     print("fetchone", item[1], item[4])
#     print(item)
#
#     # # 获取结果,抓取结果集中所有的数据，默认是从第一条开始
#     # # 元组来封装每一条记录
#     result = cs1.fetchall()
#     for item in result:
#         print(item[1], item[4])
#
#
# if __name__ == '__main__':
#     main()

# # 第一遍
# import pymysql
#
# con_sql = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', port=3306, database='JingDong',
#                           charset='utf8')
# cur_sql = con_sql.cursor()
# effect_row = cur_sql.execute('select * from goods')
# print(effect_row)
# item = cur_sql.fetchone()
# print(item[1], item[4])
#
# for item in cur_sql.fetchall():
#     print(item[1], item[4])

# 第二遍
# import pymysql
# con_sql = pymysql.connect(host='localhost', user='root',password='ZHISHAO8@gezifu',port=3306,database='JingDong',charset='utf8')
# cur_sql = con_sql.cursor()
# effect_rows = cur_sql.execute('select * from goods')
# print(effect_rows)
# first_row = cur_sql.fetchone()
# print(first_row[1], first_row[4])
# for item in cur_sql.fetchall():
# 	print(item[1],item[4])
# cur_sql.close()
# con_sql.close()
