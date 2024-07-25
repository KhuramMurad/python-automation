import os
# cwd = current working directory
print("My current working directory is : " + os.getcwd())

'''
new_path = "C:\\Users\\Khuram"
os.chdir(new_path)
print("My new path is : " + os.getcwd())

# listdir()
list_dir = old_path = os.listdir()
print(type(list_dir))
print(list_dir)


# some additional work
'''
print("my old path files contents are : \n", list_dir[1])
for file in list_dir:
    print(file)
'''
# seperator
seperator = os.sep
print("the seperator in this OS is :", seperator)
#
os.mkdir('Khuram')
print(os.listdir())
# changing name of a directory
os.rename('Khuram', 'Rumman')
print(os.listdir())
print("again creating the directory = ", os.mkdir('Khuram'))
