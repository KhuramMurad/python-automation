#from typing import Any
import paramiko
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import *
import time as t
day = date.today()
time = datetime.now()

day = date.today()
time = datetime.now()

my_custom = day.strftime("%B %d %Y")
current_time = time.strftime("%I:%M:%S %p")

# How to get 80% more than storage details
#print(dir(paramiko))
hostname = "192.168.56.101"
username = "centos"
password = "1234"
client_ = paramiko.SSHClient()
client_.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_.connect(hostname=hostname, username=username, password=password)
my_command = "free -g | grep Mem | awk '{print$7}'"

stdin, stdout, stderr = client_.exec_command(my_command)

my_output = stdout.read().decode()
print(my_output)
if int(my_output) <= 0:
    print("Mail has been sent")
    msg = MIMEMultipart()
    logo = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 40\alnafi-220930-222108.jpg"
    my_email = 'faris.ghazi.1983@gmail.com'
    password = 'adezdjgkajospltx'
    msg['Subject'] = f"MEMORY ALERT !!! Memory Alaviable: {my_output} Gb on Sever 1 at {my_custom} {current_time}"
    msg['from'] = my_email
    msg['to'] = my_email
    msg['Cc'] = 'khuram.saggu@gmail.com, khurram.murad83@gmail.com'
    body = (
        '<html><p> <b>Salam Team !!!<br></b> This is memory low alert message through Python - Hands on project in '
        'Lecture 50 <br><img \n'
        '    src="cid:alogo" width="150" height="100"></p></html>')

    msg.attach(MIMEText(body, 'html'))
    # Logo
    mylogo = open(logo, 'rb')
    msgIMAGE = MIMEImage(mylogo.read())
    mylogo.close()
    msgIMAGE.add_header('Content-ID', '<alogo>')
    msg.attach(msgIMAGE)

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(msg)
    connection.close()
else:
    print("Everything is fine")


