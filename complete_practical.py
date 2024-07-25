import json
import os
from typing import List

from cryptography.fernet import Fernet
import mysql.connector
import csv
try:
        csvfile_path = r"D:\OneDrive\Al Nafi\DevOps Track Level 4\3- Python Automation\Lecture 59\mycsvfile.csv"
        linux_json = r"D:\OneDrive\Al Nafi\DevOps Track Level 4\3- Python Automation\Lecture 59\linux.json"

        with open(linux_json) as jf:
            my_dict = json.load(jf)
            print("mysql password is being fetched and encrypted ...")
            username_mysql = my_dict['username']
            password_mysql = my_dict['password']

            message = password_mysql.encode("utf-8")
            key = Fernet.generate_key()
            f = Fernet(key)
            enc = f.encrypt(message)
            dec = f.decrypt(enc)
            pass_for_mysql = dec.decode('utf-8')

        mydb = mysql.connector.connect(host='localhost', user='mysql_user', password=pass_for_mysql, database='alnafi')
        print("CSV file is reading and storing data in database ... ")
        all_value = []
        with open(csvfile_path) as csv_file:
            csvfile = csv.reader(csv_file, delimiter=',')
            row: list[str]
            for row in csvfile:
                value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                all_value.append(value)
        query = "insert into my_df_data (filesystem,size,used,avail,usage_with_per,mounted_on,datetime,ip_address,hostname) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        my_cursor = mydb.cursor()
        my_cursor.executemany(query, all_value)
        mydb.commit()
        mydb.close()
        print("data has been inserted into the database successfully")
except Exception as e:
    print("Something is wrong please check your code : ", e)



# improved and professional code
'''
import json
import csv
import mysql.connector
from cryptography.fernet import Fernet
import logging

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

def load_configuration(config_file_path):
    try:
        with open(config_file_path) as config_file:
            config = json.load(config_file)
        return config
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        raise

def encrypt_password(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode("utf-8"))
    return encrypted_password, key

def read_csv_file(csv_file_path):
    try:
        with open(csv_file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            headers = next(reader)  # Read the header row
            data = [tuple(row) for row in reader]
        return headers, data
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
        raise

def insert_data_into_database(config, headers, data):
    try:
        mydb = mysql.connector.connect(**config['database'])
        query = "INSERT INTO my_df_data (filesystem, size, used, avail, usage_with_per, mounted_on, datetime, ip_address, hostname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        my_cursor = mydb.cursor()
        my_cursor.executemany(query, data)
        mydb.commit()
        mydb.close()
        print("Data has been inserted into the database successfully")
    except Exception as e:
        logging.error(f"Error inserting data into the database: {e}")
        raise

if __name__ == "__main__":
    try:
        config_file_path = "config.json"
        config = load_configuration(config_file_path)

        linux_json_path = config['linux_json_path']
        username_mysql = config['database']['user']
        password_mysql = config['database']['password']

        encrypted_password, key = encrypt_password(password_mysql)

        csvfile_path = config['csvfile_path']
        headers, all_value = read_csv_file(csvfile_path)

        insert_data_into_database(config, headers, all_value)
    except Exception as e:
        print("Something went wrong, please check the logs for details.")
'''