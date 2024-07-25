import re

'''
mytext="My 192.168.1.8 jboss server ip address is  \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345"
pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
myfind=(re.findall(pattern,mytext))
print(myfind)

mytext = "My 192.168.1.8 jboss server ip address is"
print(re.split('[a-c]','0a2ALI7',re.I))
print(re.split('[a-z, A-Z]','aquickbrownfox123456789'))

mystring = (re.split('[a-z, A-Z]','aquickbrownfox123456789'))
for i in mystring:
    print(i.endswith('aqu', 5,8))

myword = "Abdeali Dodiya from bangalore, We are leaning python course and in this python course will lear two version like python2 and python3 course"
pattern = r"\bcourse\b"
print(re.sub(pattern, 'COURSE', myword))
print(myword)  # no change in original string
'''
