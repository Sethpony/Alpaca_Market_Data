import pymysql

connection = pymysql.connect(host='database-1.ck62t6bhkvok.us-east-2.rds.amazonaws.com', user='admin',  password='Pass123!', database='test')

with connection:
    # with connection.cursor() as cursor:
    #     sql = "create database market_data"
    #     cursor.execute(sql)

    # with connection.cursor() as cursor:
    #     sql = "SELECT * FROM TEST"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     print(result)

    with connection.cursor() as cursor:
        # sql = "create table market_data(stock varchar(32), metric varchar(32))"
        # cursor.execute(sql)

        # sql = "INSERT INTO market_data(`stock`, `metric`) VALUES ('test3', 'test4')"
        # cursor.execute(sql)

        sql = "SELECT * FROM market_data"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


    connection.commit()