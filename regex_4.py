import re

mytext = "My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
'''
print(re.findall(pattern, mytext))
myiter = (re.finditer(pattern, mytext))
print(myiter)  # object created
for i in myiter:
    print(i)  # check span value in output to know about starting and ending index values

my_match = (re.findall(pattern, mytext))
print(type(my_match))
for i in my_match:
    print("The IP address is : ", i)

myiter = (re.finditer(pattern, mytext))
for i in myiter:
    print(i.group())

mytext="We are learning python automation course, In devops course python is very important"
#pattern=r"\bcourse\b"
pattern = re.compile('course') # usage of re.complie() method. it is very fast as compare to pattern = r"\bcourse\b" methhod, it creats an object that can be called anywhere.

print(re.findall(pattern,mytext))

mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.search(pattern,mytext))
print('We are found some string from pattern',myfind)
print('We are found some string from pattern',myfind.group())
print('Starting Index',myfind.start())
print('Ending Index',myfind.end())
print('Index length is :',myfind.end()-myfind.start())
'''
mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"ABD\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.search(pattern,mytext))

if myfind:
    print('We are found some string from pattern',myfind.group())
else:
    print("Sorry, No match found")
