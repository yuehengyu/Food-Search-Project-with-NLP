import pymysql
import  pymysql.cursors

connection=pymysql.connect(host='localhost',
                           user='root',
                           password='Abc,123.',
                           db='house',
                           port=3306,
                           charset='utf8')

try:
    #获取一个游标
   with connection.cursor() as cursor:
       sql='select * from income'
       cout=cursor.execute(sql)
       # print(cout)

       for row in cursor.fetchall():
           # print(row)

            #注意int类型需要使用str函数转义
           print("zip_code: "+str(row[0])+" mean: "+str(row[1])+" Median: "+str(row[2])+" Stdev: "+str(row[3]))
       connection.commit()

finally:
    connection.close()
