# write a file
'''

with open('another_testfile.txt', 'w') as newfile:
    write_file = newfile.write("This is a new txt file created by Python\n Text entered again")
    print(write_file)

# append the file

with open('another_testfile.txt', 'a') as newfile: # 'a' mode appends and creates the file
    write_file = newfile.write("This is a new text file created by Python\nText entered again")
    write_file = newfile.write("\nThis text is entered after setting the 'Append' mode")
    print(write_file)


mylist = ['This', 'data', 'is', 'from', 'list']
with open ('list_file.txt', 'w') as list:
    for i in mylist:
        list.write(i+'\n')
'''

# write date with a loop

for i in range(11):
    with open('loop.txt', 'a') as loop_file: # 'w' mode will overwrite the data
        #loop_file.write(f"Line No. {i}" + '\n')
        loop_file.write('This is from loop\n')