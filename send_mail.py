import smtplib
import time
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from mails_list import FINAL_LIST
from html_str import HTML_STR


#  Enable less secure apps here: https://myaccount.google.com/lesssecureapps
class SendMails():

    def __init__(self, my_mail, from_str, my_password, subject, my_file=None, text='', recipients=None):
        """
        my_mail = 'my_mail@mail.com'
        from_str = 'My Name'
        my_password = 'password'
        subject = 'Hello!'
        my_file = 'file.txt' - not required
        text = 'Hi there!' - not required. If not specified text from html_str.py is used.
        recipients = [[...], ] - not required. If not specified list from mails_list.py is used.
        """
        self.my_mail = my_mail
        self.from_str = from_str
        self.my_password = my_password
        self.subject = subject
        self.my_file = my_file
        self.text = text or HTML_STR
        self.recipients = recipients or FINAL_LIST

    def get_file(self):
        if self.my_file:
            with open(self.my_file, "rb") as f:
                part = MIMEApplication(
                    f.read(),
                    Name=basename(self.my_file)
                )
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(self.my_file)
            return part
        else:
            return None

    def conect_to_gmail_server(self):
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mail_server.ehlo()
        mail_server.login(self.my_mail, self.my_password)
        return mail_server

    def create_msg(self, recipients):
        msg = MIMEMultipart()
        recipients_str = ', '.join(recipients)
        print(recipients_str)
        msg['To'] = recipients_str
        msg['From'] = self.from_str
        msg['Subject'] = self.subject
        # msg.attach(MIMEText(text))
        html = self.text.format(id=recipients[0], recipients=recipients_str)
        msg.attach(MIMEText(html, 'html'))
        file_part = self.get_file()
        if file_part:
            msg.attach(file_part)
        return msg

    def send_mails(self):
        mail_server = self.conect_to_gmail_server()

        for idx, recipients in enumerate(self.recipients):
            msg = self.create_msg(recipients)

            mail_server.sendmail(self.my_mail, recipients, msg.as_string())
            print("{}: {}".format(idx, recipients))
            time.sleep(1)

        mail_server.close()
