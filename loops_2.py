
# while loop
''''
i= 1

while i <= 10:
    print(i)
    i=i+1


# in reverse order

i= 10
while i >=0:
    print(i)
    i= i-1
'''

import os
print(list(os.walk(os.getcwd())))
for roots, dirs, files in (list(os.walk(os.getcwd()))):
   if len(dirs) != 0:
       print(roots)
       for i in files:
           print(os.path.join(roots,i))

#print(len(os.path.join(roots,i))) # total no of files in this path
