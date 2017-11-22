import sys
from html_str import HTML_STR_2
from collections import OrderedDict
from send_mail import SendMails


# START SETTINGS
ASYNC_CONTACTS_SEARCH_PATH = '/home/vladimir/async_contacts_search'
CSV_FILE_PATH = ASYNC_CONTACTS_SEARCH_PATH + '/contacts_csv/02_10_17/contacts_total.csv'
HTML_TEXT = HTML_STR_2
LIMIT_MAILS_PER_DAY = 180
start_from_site = "http://hallspot.com/"  # start sending from this site
# END SETTINGS


sys.path.append(ASYNC_CONTACTS_SEARCH_PATH)

from csv_contacts_reader import CSVContactsReader


reader = CSVContactsReader(CSV_FILE_PATH)
contacts = reader.get_clean_contacts()
ordered_contacts = OrderedDict(sorted(contacts.items(), key=lambda t: t[0]))

limit_message = ''
limit_counter = 0
if start_from_site:
    is_sending_on = False
else:
    is_sending_on = True
recipients = []  # [[...], ]

for site in ordered_contacts:
    if is_sending_on or site == start_from_site:
        is_sending_on = True
        site_mails = ordered_contacts[site]
        site_mails = list(site_mails)
        limit_counter += len(site_mails)
        if limit_counter <= LIMIT_MAILS_PER_DAY:
            recipients.append(site_mails)
        else:
            limit_message = 'Done. "{}" is out of limit.'.format(site)
            print(limit_message)
            break

# SETTINGS
sd = SendMails(
    my_mail='',
    from_str='Vova Gosha',
    my_password='',
    subject='Python / IOS developer',
    my_file='/home/vladimir/Downloads/CV Vova Python IOS developer.pdf',
    text=HTML_TEXT,
    recipients=recipients,
)

sd.send_mails()

print(limit_message)
