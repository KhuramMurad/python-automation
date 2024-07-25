import csv
import smtplib
from email.message import EmailMessage

my_mail = "faris.ghazi1983@gmail.com"
password = "adezdjgkajospltx"
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls() # Transport Layer Security
msg = EmailMessage()
msg['Subject'] = "This is lecture 39 Python Automation SMTP Module"
msg['From'] = my_mail
msg['To'] = my_mail
msg['Cc'] = 'khuram.saggu@gmail.com'
msg.set_content("Asalam o Alykum !!! Team Hope you are doing well, This is a test mail to check SMTP Server")
# Attachement
with open('for_attachement.csv', 'rb') as myfile:
    attach_File = myfile.read()
    file_name = myfile.name
msg.add_attachment(attach_File, maintype='application', subtype='octat-stream', filename=file_name)
connection.login(user=my_mail, password=password)
#connection.sendmail(from_addr=my_mail, to_addrs="faris.ghazi1983@gmail.com", msg="Salam, This is test mail")
connection.send_message(msg)
connection.close()
print("email has been sent")
