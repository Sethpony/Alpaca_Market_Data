import pymysql

connection = pymysql.connect(host='database-1.ck62t6bhkvok.us-east-2.rds.amazonaws.com', user='admin', password='Pass123!', database='test')

with connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO test (`employee`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #why need to commit?
    connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT * FROM test"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)


# cursor = db.cursor()
# print(cursor)

#CREATE DATABASE
#sql = '''create database test'''
#cursor.execute(sql)

# sql = 'CREATE TABLE test(employee varchar(32), password varchar(32))'
# cursor.execute(sql)

# sql = "INSERT INTO test (`employee`, `password`) VALUES (%s, %s)"
# cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#
# print(cursor.execute("select * from test"))



