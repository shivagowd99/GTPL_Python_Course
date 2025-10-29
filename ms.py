import mysql.connector

con=mysql.connector.connect(host="localhost",user="root", passwd="1234",database="student")
my_cursor=con.cursor()


my_cursor.execute('select * from data')
# res=my_cursor.fetchall() # which is gives all employees data
res=my_cursor.fetchone()
for i in res:
    print(i)