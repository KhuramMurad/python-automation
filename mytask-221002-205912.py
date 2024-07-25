import schedule
import time as t
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import datetime

def abd():
    day = datetime.today()
    time = datetime.now()

    my_custom = day.strftime("%B %d %Y")
    current_time = time.strftime("%I:%M:%S %p")

    filename = r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 40\test.txt"
    mylogo = r"C:\Users\AbdealiDodiya\Desktop\DevOps\Python\Lecture 40\alnafi.jpg"
    msg = MIMEMultipart()

    my_mail = "automation52786@gmail.com"
    password = "nrjxoxmahyxzybvm"
    msg['Subject'] = f"Citrix connection alert {my_custom} {current_time}"
    msg['From'] = my_mail
    msg['To'] = my_mail
    msg['Cc'] = 'abdealipython@gmail.com'

    body = """ 
    <html><p> <b> <i>Hi Team,<br> This is testing email server via python script. <b> <i> <br> <img src="cid:alogo" width="100" height="50"></p> </html> 
    """
    msg.attach(MIMEText(body, 'html'))

    ###LOGO section
    filelogo = open(mylogo, 'rb')
    msgIMAGE = MIMEImage(filelogo.read())
    filelogo.close()
    msgIMAGE.add_header('Content-ID', '<alogo>')
    msg.attach(msgIMAGE)

    # ATTACHMENT section
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=%s" % filename)
    msg.attach(part)

    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()  # TLS transport layer security

    connection.login(user=my_mail, password=password)
    connection.send_message(msg)
    connection.close()
    print("Mail has been sent")

schedule.every().day.at("21:15").do(abd)

while True:
    schedule.run_pending()
    t.sleep(1)