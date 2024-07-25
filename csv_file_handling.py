'''
csv_data = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 37\servershealth-220925-204801.csv"
with open (csv_data, 'r') as datafile:
    mydata = datafile.readlines()
    # medhod 1
    mydata = datafile.read()
    print(mydata)

    # method 2
    mydata = datafile.readlines()
    print(mydata)
    # method 3
    for i in mydata:
        #print(i)
        print(i.strip("\n").split())
'''
import csv

csv_data = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 37\servershealth-220925-204801.csv"
with open(csv_data) as mydata:
    data = csv.reader(mydata)
    # print(data) # object is created
    for each in data:
        print(each)
