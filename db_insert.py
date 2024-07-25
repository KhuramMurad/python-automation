try:
    import mysql.connector
    from datetime import *
    my_data = input("Please enter the name you want to delete : ")
    time = datetime.now()
    my_time = time.strftime("%Y-%m-%d %H:%M:%S")

    mydb = mysql.connector.connect(host="localhost", user="mysql_user", password="test123", database="alnafi",
                                   auth_plugin='mysql_native_password')

    cur = mydb.cursor()

    # insert query
    data = "'rezz@123'"
    sql = f" DELETE from trainer_details where fname = '{my_data}' "

    cur.execute(sql)
    # fetching data
    sql_select = """ select * from trainer_details """
    cur.execute(sql_select)
    result = cur.fetchall()
    for data in result:
        print(data)

    mydb.commit()

    mydb.close()
except Exception as e:
    print("something is wrong : ", e)