import smtplib
import time
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from mails_list import FINAL_LIST
from html_str import HTML_STR

#  Enable less secure apps here: https://myaccount.google.com/lesssecureapps
my_mail = 'my_mail@mail.com'
from_str = 'My Name'
my_password = 'password'
subject = 'Hello!'
my_file = 'file.txt'
text = HTML_STR


def send_mail():
    gmailUser = my_mail

    with open(my_file, "rb") as f:
        part = MIMEApplication(
            f.read(),
            Name=basename(my_file)
        )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(my_file)

    mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mailServer.ehlo()
    mailServer.login(gmailUser, my_password)

    for idx, recipient in enumerate(FINAL_LIST[940:]):
        msg = MIMEMultipart()
        msg['To'] = recipient
        msg['From'] = from_str
        msg['Subject'] = subject
        # msg.attach(MIMEText(text))
        msg.attach(MIMEText(text.format(recipient), 'html'))
        msg.attach(part)

        mailServer.sendmail(gmailUser, recipient, msg.as_string())
        print("{}: {}".format(idx, recipient))
        time.sleep(1)

    mailServer.close()


send_mail()
