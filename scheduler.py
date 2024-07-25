import schedule
import time as t
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import *

def my_task():

    day = date.today()
    time = datetime.now()

    my_custom = day.strftime("%B %d %Y")
    current_time = time.strftime("%I:%M:%S %p")
    file = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 40\MIME_test.txt"
    logo = r"D:\OneDrive\Al Nafi Emerging Technologies Study Material\DevOps Track Level 4\3- Python Automation\Lecture 40\alnafi-220930-222108.jpg"
    msg = MIMEMultipart()
    my_email = 'faris.ghazi.1983@gmail.com'
    password = 'adezdjgkajospltx'
    msg['Subject'] = f"MIMEMultipart email test {my_custom} {current_time}"
    msg['from'] = my_email
    msg['to'] = my_email
    msg['Cc'] = 'khuram.saggu@gmail.com, khurram.murad83@gmail.com'
    body = """<html><p> <b>Salam Team !!!<br></b> This is testing email via MIMEMultipart module Python <br><img 
    src="cid:alogo" width="150" height="100"></p></html>"""

    msg.attach(MIMEText(body, 'html'))
    # Logo
    mylogo = open(logo, 'rb')
    msgIMAGE = MIMEImage(mylogo.read())
    mylogo.close()
    msgIMAGE.add_header('Content-ID', '<alogo>')
    msg.attach(msgIMAGE)
    # Attachment
    attachment = open(file)
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=%s' % file)
    msg.attach(part)

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(msg)
    connection.close()
    print("email has been sent successfully")


'''
    now = datetime.today()
    print("Current time is : ", now)
    print("This is a testing message to schedule a task in Python")


job1 = schedule.every(2).seconds.do(my_task) # seconds

job2 = schedule.every(1).minutes.do(my_task) # minutes
'''

job3 = schedule.every().day.at("19:05").do(my_task) # specif time today
while True:
    # this syntax is compulsory
    schedule.run_pending() # to check if any scheduled jobs are due to run.
    t.sleep(1)