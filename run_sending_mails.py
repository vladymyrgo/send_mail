import sys
# settings
ASYNC_CONTACTS_SEARCH_PATH = '/home/vladimir/async_contacts_search'
CSV_FILE_PATH = ASYNC_CONTACTS_SEARCH_PATH + '/contacts_csv/02_10_17/contacts_total.csv'

sys.path.append(ASYNC_CONTACTS_SEARCH_PATH)

from collections import OrderedDict
from send_mail import SendMails
from csv_contacts_reader import CSVContactsReader


reader = CSVContactsReader(CSV_FILE_PATH)
contacts = reader.get_clean_contacts()
ordered_contacts = OrderedDict(sorted(contacts.items(), key=lambda t: t[0]))

recipients = []

for site in ordered_contacts:
    site_mails = ordered_contacts[site]
    site_mails = list(site_mails)
    recipients.append(site_mails)

# settings
sd = SendMails(
    my_mail='',
    from_str='Vladimir Gosha',
    my_password='',
    subject='Hello. This is test!',
    my_file=None,
    text='',
    recipients=recipients,
)


sd.send_mails()
