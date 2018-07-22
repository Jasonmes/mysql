import pymysql


def main():
    # 创建连接
    conn = pymysql.connect(host='localhost', user='root', password='mysql', port=3306, database='db_jingdong',charset='utf8')

    # 创建游标 pymysql.cursors.DictCursor:取得字典游标，取得的结果以字典的形式呈现的
    cs1 = conn.cursor(cursor=pymysql.cursors.DictCursor)   # ctrl+alt+v

    sql="select price,name from goods"
    # 执行查询
    affect_rows=cs1.execute(sql)

    print("影响的行数:",affect_rows)

    # 获取结果,抓取结果集中的一条数据，默认是从第一条开始
    # 一条记录封装在元组中  --》(1, 'r510vc 15.6英寸笔记本', 1, 2, Decimal('3399.000'), b'\x01', b'\x00')
    item=cs1.fetchone()
    print(item)
    print("fetchone",item["name"],item["price"])

    # 获取结果,抓取结果集中所有的数据，默认是从第一条开始
    # 元组来封装每一条记录
    result=cs1.fetchall()
    for item in result:
        print(item["name"],item["price"])


if __name__ == '__main__':
    main()

