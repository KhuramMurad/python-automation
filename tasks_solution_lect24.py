'''
import os
import platform

if platform.system() == 'Linux':
    # List .txt files in the current directory for Linux
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".txt"):
            print(filename)
elif platform.system() == 'Windows':
    # List .txt files in the C:\ directory for Windows
    windows_directory = "C:\\"
    for filename in os.listdir(windows_directory):
        if filename.endswith(".txt"):
            print(filename)
else:
    print("Unsupported operating system")

'''

# Task 2
import os
find = input("Enter the file to search : ")
for roots,dirs,files in os.walk("C:\\"):
    for i in files:
        if i == find:
            print(os.path.join(roots,i))

