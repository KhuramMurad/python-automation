import my_name
print(my_name.lname) # "my_name" is the file that holds "lname" variable in it that is being called in present file.
print(my_name.fname) # similary "fname" variable is also imported from "my_name" file

# it can be done as below
import my_name as name # name is a random word as "alias"
print(name.lname)
print(name.fname)


# most convenient way
from my_name import *
print(lname, fname)


