import mysql.connector
#print(dir(mysql.connector))

mydb = mysql.connector.connect(host='localhost', user='root', password='1234', database='AlNafi')
cur = mydb.cursor()
sql = '''select * from trainer_details'''
cur.execute(sql)
result = cur.fetch()
mydb.close()
