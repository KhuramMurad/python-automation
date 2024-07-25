# for list
mylist = [1,2,3,4,5]
mylist.pop(2)
print(mylist)

'''
my_tuple = (1,2,3,4,5)
my_tuple.pop(2)
print(my_tuple)
AttributeError: 'tuple' object has no attribute 'pop'
'''
# with distionary
cred = {'username' : 'khurammurad' , 'pass' : 'kms@123'}
cred.pop('pass') # the 'pass' key value pair is removed
print(cred)

mydict = {1: 3, 5: 10}
print(max(mydict)) # by-default it performs max function or operation on keys
print(max(mydict.values())) # to get min or max values use .value() method

print(min(mydict))
print(min(mydict.values()))

# to check if a specific key is in the dictionary

cred1 = {'username' : 'khurammurad' , 'pass' : 'kms@123' , 'domain' : 'khuram.com'}
print(cred1)
if 'domain' in cred1:
    print("the key 'domain' is present in the dictionary")
else:
    print("Sorry !!! the key is not present in the dictionary")


# nested dictionary
information = {
    1 : {'name' : 'Khuram' , 'pass' : 'kms@123', 'server' : 'Linux'},
    2 : {'name' : 'Raza' , 'pass' : 'rezz@123', 'server' : 'Apache'},
    3 : {'name' : 'Rumman Khuram' , 'pass' : 'rummi@123', 'server' : 'windows'},

    }

print(information)
print(information[3]['name'])
print(information[2]['name'])
print(information[1]['name'], "has the server : " , information[1]['server'])


