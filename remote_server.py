import paramiko
#print(dir(paramiko))
hostname = "192.168.56.101"
username = "centos"
password = "1234"
client_ubuntu = paramiko.SSHClient()
client_ubuntu.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_ubuntu.connect(hostname=hostname, username=username, password=password)
#my_command = "df -h"
my_command = input("Enter a valid Linux Command : ")
stdin, stdout, stderr = client_ubuntu.exec_command(my_command)
#mycmd_out = stdout.read()
#mycmd_out = stdout.readlines() # to convert to lists .readlines()
my_command = stdout.read().decode() #and .decode() to convert to string , in this case no for loop is needed.
print(my_command)
#print(mycmd_out)
client_ubuntu.close()
'''
for i in mycmd_out:
    print(i.strip("\n"))
'''