import csv

mypath=r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 37\servershealth.csv"
with open(mypath) as datafile:
    data=csv.reader(datafile)
    for each in data:
        print(each)
