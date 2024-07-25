import sys
'''
print(sys.version)
print(sys.version_info)
print(sys.path)

print("Khuram")
print("Murad")

print("sys exit start")

print("Saggu")
#sys.exit()
print("Exit over")


print("Khuram")
print(sys.argv[1])
'''

########### Script for Linux #############
import os
import sys

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} requires 2 parameters \n for example service name docker, apache2 and action for example status, start, stop ")
    sys.exit()
else:
    status = sys.argv[1]
    service = sys.argv[2]
    os.system(f'systemctl {status} {service}')
