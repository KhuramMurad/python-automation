# for loop
'''
#i = 0
for i in range(1,10,2):
    print(++i)

mylist = ['Khuram', 'Murad', 'Islamabad', 'Pakistan']

for i in mylist:
    print(i)
'''
# dictionary
my_dict = {'Name': 'Khuram', 'Age': 40, 'Country': 'Pakistan'}

print(my_dict.keys())
print(my_dict.values())
##########################
for key, value in my_dict.items(): # remember !!! key and value are variables it can be k,v or a,b etc.
    print(key, value)
# for jut keys
print("just keys of the dictionary")
for key in my_dict.keys():
    print(key)
# for just values
print("just values of the dictionary")
for value in my_dict.values():
    print(value)
