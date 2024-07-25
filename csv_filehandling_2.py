'''
import csv
my_file = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 38\servershealth-220930-214947.csv"
my_list = [13,'10.226.17.110','WINDOWS-11','d6:60:7f:6e:f6:5c','51 GB']
with open(my_file, 'a') as csv_file:
   csv_write = csv.writer(csv_file)
   csv_write.writerow(my_list)


import csv
list1 = [1, 'Khuram', 'DevOps', 'Islamabad']
list2 = [2, 'Raza', 'Doctor', 'Russia']

with open('new_data.csv', 'w', newline='') as newfile:
   csv_data = csv.writer(newfile)
   csv_data.writerow(list1)
   csv_data.writerow(list2)
'''
import csv

data = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 38\servershealth-220930-214947.csv"
newlist = []
with open(data) as csv_file:
    csv_data = csv.reader(csv_file)
    # print(csv_data)
    header = next(csv_file) # to remove header of CSV file
    for each in csv_data:
        print(each)
        if each[2] == "RHEL":
            #print(each[1])  # to display only IP address of RHEL OS
# to insert it into a new list
            newlist.append(each)
#print(newlist)
out_put_csv = 'newcsv.csv'
# to create a new CSV file from this data
with open(out_put_csv, 'w', newline='') as newcsv:
   new_data = csv.writer(newcsv)
   new_data.writerow(header)
   new_data.writerows(newlist)
print(f"new data is filtered and added to new file")
#
# Print the header row
print(",".join(header))
# Print the filtered data
for row in newlist:
    print(",".join(row))