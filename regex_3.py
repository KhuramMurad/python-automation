import re
'''
myword="Abd$%*eal2@1i Dodiya from bangalore , Python is very good language abdealipython@gmail.com We are learning python and in this course we will learn two version such python2 and python3, We will learn Python selenium in this coursesss"
pattern=r"\bpython\d\b"
print(re.findall(pattern,myword))

mytext="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11"
pattern=r"\d{3}.\d{3}.\d{1}.\d{2}"
print(re.findall(pattern,mytext))

mytext="My jboss server ip address is 192.168.1.8 \nMy Docker server ip address is 192.168.1.11 \n My broadcast addres is 255.255.255.255 \n My invalid address 192.168.1234.12345 \n my invalid address is 0..12.34"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" # to avoid wrong IP addresses. use "\" in every octate but not in last one.
print(re.findall(pattern, mytext))
'''
# Multiline
import re
mytext = """My jboss server ip address is 192.168.1.8
My Docker server ip address is 192.168.1.11
My broadcast addres is 255.255.255.255
My invalid address 192.168.1234.12345
my invalid address is 0..1.3
"""
#pattern = r"^My"
#print(re.findall(pattern, mytext, re.M))
pattern = r"^My"
print(re.findall(pattern, mytext, re.M | re.I))

