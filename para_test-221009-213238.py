import paramiko
hostname="192.168.1.11"
username="aadmin"
password= "123@abd"
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)
mysftp = client.open_sftp()
mysftp.chdir('/home/aadmin/lect51')
file=mysftp.open('test.csv')
print(file.read())
mysftp.close()
client.close()