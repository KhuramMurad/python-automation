#from typing import Any

import paramiko

# How to get 80% more than storage details
#print(dir(paramiko))
hostname = "192.168.56.101"
username = "centos"
password = "1234"
client_ubuntu = paramiko.SSHClient()
client_ubuntu.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_ubuntu.connect(hostname=hostname, username=username, password=password)
my_command = "df -h"

stdin, stdout, stderr = client_ubuntu.exec_command(my_command)

my_output = stdout.readlines()
print(my_output)
client_ubuntu.close()