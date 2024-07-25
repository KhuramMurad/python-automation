import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="mysql_user", password="test123", database="alnafi", auth_plugin='mysql_native_password')
#connection object creation
cur = mydb.cursor()
#fetch data
#sql = '''select * from trainer_details'''

# execution
'''
The error message you are getting is because you are not passing the SQL operation to the execute() function. The execute() function takes two positional arguments:
•	The SQL operation to be executed.
•	A tuple of parameters for the SQL operation (optional).
To fix the error, you need to pass the SQL operation to the execute() function. For example:
'''
#cur.execute(input("Enter the mysql command : "))
cur.execute('SELECT * FROM my_df_data')


#cur.execute()
result = cur.fetchall()
for i in result:
    print(i)
#print(result)
mydb.close()

