# os.path()
import os

#mypath = "D:\\OneDrive\\Al Nafi Emerging Technologies Study Material\\DevOps Track Level 4\\3- Python Automation\\Lecture 19"

'''
print(mypath)
print(os.path.isfile(mypath)) # False
print(os.path.isdir(mypath)) # True



# if condition
if os.path.exists(mypath):
    if os.path.isdir(mypath):
        print(f"{mypath} is a directory")
    else:
        print(f"{mypath} is a file")
else:
    print(f"the path {mypath} is not correct , please enter the correct path")
'''

##################

# os.path.join()

mypath = "D:\\OneDrive"
mychildpath = "Al Nafi Emerging Technologies Study Material"

check = os.path.join(mypath,mychildpath)
print(f"the joined path is  {check}")
print("the path seperator is : ", os.path.sep) # to check seperator
# os.path.getsize(<variable>)  to get size in bytes


