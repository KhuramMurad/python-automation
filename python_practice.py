import os
myfiles=os.listdir()
print(myfiles)
myext=myfiles[1].split(".")
print(myext[0])
