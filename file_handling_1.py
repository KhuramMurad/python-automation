''''
file = open('test_file.txt')
contents_of_file = file.read()
print(contents_of_file)
file.close() # this step is compulsory because it ocupy the resources and an opened file must be closed
'''

# 2nd method

with open('test_file.txt') as file:
    #contents_of_file = file.read()
    #print(contents_of_file)  # this method does not required to close the file
    #print(file.read())
    contents_of_file = file.readlines()
    #print(contents_of_file)
    for i in contents_of_file:
        words = i.split()
        #print(i)
        print(words)



