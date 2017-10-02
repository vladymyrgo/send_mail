# send_mail

Sending mails via Gmail

### Example:
```
from send_mail import SendMails
sm = SendMails(
    my_mail='my_mail@mail.com',
    from_str='My Name',
    my_password='***',
    subject='Hello!',
    my_file='file.txt',
    text='The long story',
    recipients=[[...], ]  # lists in list!
)
sm.send_mails()
```

### Sending mails to sites that were founded by async_contacts_search (other repo):

run run_sending_mails.py Change settings in this file first.
