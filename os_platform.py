import os
import platform

'''
#print(dir(platform))
print(platform.system())
print(platform.processor())
print(platform.architecture())
print(platform.node()) # shows hostname
print(platform.platform())
print(platform.machine())
uname = platform.uname()
print(uname)
print(platform.release())
'''
################ plateform independent script in Python ##################

operating_system = platform.system()

if operating_system == "Windows":
    command = input(f" you are on {operating_system} please enter the command : ")
    os.system(command) # for Windows
elif operating_system == "Linux":
    command = input(f" you are on {operating_system} please enter the command : ")
    os.system(command) #" for Linux"
else:
    print("Sorry !!! please contact the admin ")

