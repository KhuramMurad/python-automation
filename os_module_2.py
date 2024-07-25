'''
###########################TASK###########################
import os

# list only '.docx' file

files = os.listdir()
#ilter = files[2].split()
#print(filter)
print(files)

# 2nd way
search_item = input("Please enter the item to be searched : ")
found = False
for item in files:
    if item == search_item:
        found = True
        break

if found:
    print(f"The {search_item} is found in the list")
else:
    print(f"sorry !! the {search_item} is not found in the list")

'''
###################################################################################
import os
#os.walk()

#find = (list(os.walk(os.getcwd())))
#print(type(walk))
#print(find)

#for best output run this file in Linux

#print(os.system('dir')) # use 'ls' for Linux

#command = os.popen('dir').read()
#print(command)
'''
Task done with Method 1 with "Bash + Python"
import os
version = os.popen("""cat /etc/os-release | awk -F= 'NR==3 {print $2}' | sed 's/"//g'""").read()
print("The OS Version is = ", version)
'''




