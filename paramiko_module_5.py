import paramiko
'''
hostname = "192.168.56.101"
username = "root"
password = "1234"
client_linux = paramiko.SSHClient()
client_linux.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_linux.connect(hostname=hostname, username=username, password=password)
my_ftp = client_linux.open_sftp()
my_ftp.get('/root/Python-Automations/lecture51/server.csv','test.csv') # name server.csv can be change to test.csv
my_ftp.close()
client_linux.close()
'''
# now from WIndows to Linux
hostname = "192.168.56.101"
username = "root"
password = "1234"
client_linux = paramiko.SSHClient()
client_linux.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_linux.connect(hostname=hostname, username=username, password=password)
my_ftp = client_linux.open_sftp()
my_ftp.chdir('/root/Python-Automations/lecture51')
#my_ftp.put('test.csv','test_linux.csv') # full local path can also be given
#print(my_ftp.listdir()) # to list the fles in current location
#print(my_ftp.stat('test_linux.csv')) # to check the details of the remote file
# to append data in remote location
#file = my_ftp.open('test_linux.csv', 'a')
# to read data from remote location
file = my_ftp.open('test_linux.csv')
print(file)

#file.write('2,Server-Khuram,192.168.1.11')
# to read data
print(file.read())


my_ftp.close()
client_linux.close()
