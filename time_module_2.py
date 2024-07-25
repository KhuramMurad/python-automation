#from datetime import datetime
# strftime() --> date to string
'''
time = (datetime.now())
print(time)
print(type(time))
custom_time = time.strftime("%I:%M:%S %p %B %d %Y")
print("The custom Time & Date is : ", custom_time)
print(type(custom_time)) # datetime object is converted to string with "strftime()" method or function

# strptime() --> string to date
mydate = '11:32 56 17-09-2023'
print(type(mydate))
time = datetime.strptime(mydate, "%H:%M %S %d-%m-%Y")
print("string to date ",time)
print(type(time))


import time
import datetime

seconds = time.time()
print(seconds)
#time = datetime.datetime.fromtimestamp(seconds)
time = time.ctime(seconds) # 2nd method
print(time)

import time
from datetime import datetime
tuple1 = time.localtime()
print(tuple1)
current_time = time.strftime('%d/%m/%Y , %H:M:%S %p')
print(current_time)
'''
import time
'''
print("Time message 0")
time.sleep(1)
print("Time message 2")
time.sleep(3)
print("Time message 3")
time.sleep(5.4)
print("Time message 4")

for i in range(6): # time sleep through for loop to be used in Selinium InnSha Allah for web scraping
    print(i)
    time.sleep(1)

import os
from datetime import datetime
myfiles = os.path.getctime(os.getcwd())
print(myfiles)
print(datetime.fromtimestamp(myfiles))
'''