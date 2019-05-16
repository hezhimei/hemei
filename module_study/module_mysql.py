# /usr/bin/env python
# coding:utf-8

'''
mysqldb/pymysql常用方法：
    mysqldb.connect 建立和MySQL数据库的连接
    cursor=conn,cursor()  通过上一步建立的连接获取个cursor对象
    cursor.execute(sql)  执行SQL语句，但返回结果不是SQL执行的结果，是此SQL执行后受影响的行数
    cursor.fetchall()  获取SQL执行的所有结果，返回结果是个嵌套的元组
    cursor.fetchone()  获取SQL执行的结果，只获取第一条
    cursor.close(),conn.close()  关闭连接和cursor
'''