import pymysql

db = pymysql.connect(host='database-1.ck62t6bhkvok.us-east-2.rds.amazonaws.com', user='admin', password='Pass123!', database='test')

cursor = db.cursor()
print(cursor)

#sql = '''create database test'''
#cursor.execute(sql)

# sql = 'CREATE TABLE test(employee varchar(32), password varchar(32))'
# cursor.execute(sql)

sql = "INSERT INTO test (`employee`, `password`) VALUES (%s, %s)"
cursor.execute(sql, ('webmaster@python.org', 'very-secret'))


print(cursor.execute("select * from test"))



