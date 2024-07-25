import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import  encoders
from datetime import *
import time as t

day=date.today()
time=datetime.now()

my_custom=day.strftime("%B %d %Y")
current_time=time.strftime("%I:%M:%S %p")



msg=MIMEMultipart()

my_mail="automation52786@gmail.com"
password="nrjxoxmahyxzybvm"
msg['Subject']= f"Citrix connection alert {my_custom} {current_time}"
msg['From']= my_mail
msg['To'] = my_mail
msg['Cc'] = 'abdealipython@gmail.com'


body = """ 
<html><p> <b> <i>Hi Team,<br> This is testing email server via python script. <b> <i> <br></p> </html> 
"""
msg.attach(MIMEText(body,'html'))


connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()       #TLS transport layer security


connection.login(user=my_mail,password=password)
connection.send_message(msg)
connection.close()
