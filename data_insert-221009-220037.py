try:
    import mysql.connector
    from datetime import *
    mydata= input("Enter the name fname which you want to remove data from mysql")
    time=datetime.now()
    mycustom = time.strftime("%Y-%m-%d %H:%M:%S")
    mydb= mysql.connector.connect(host="192.168.1.8",user="mysql_user",password="test123",database="alnafi")
    #mysql connection object create
    cur = mydb.cursor()
    #Fetching data

    sql = f"delete from trainer_details where fname='{mydata}'"


    #Executing data for update query
    cur.execute(sql)
    mydb.commit()

    #Fetching mysql data
    select_sql = """ select * from trainer_details """
    cur.execute(select_sql)
    result = cur.fetchall()
    for data in result:
        print(data)

    mydb.close()
except Exception as e:
    print("Something issue please check your input", e)
