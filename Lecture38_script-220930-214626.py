import paramiko
hostname = "192.168.1.6"
username="aadmin"
password = "123@abd"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, username=username, password=password)
mysftp = client.open_sftp()
mysftp.put('myfile.csv','myfile.csv')
mysftp.close()
client.close()