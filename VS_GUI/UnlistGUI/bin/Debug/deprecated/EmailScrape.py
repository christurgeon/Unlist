import imaplib
import email
import smtplib
import time
import re
from bs4 import BeautifulSoup
import quopri
FROM_EMAIL  = ""
FROM_PWD    = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# This function is adapted from the link
# https://codehandbook.org/how-to-read-email-from-gmail-using-python/
# Used to connect and fetch emails from Gmail
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )
           # print(data)
            file = open("body.html", "w")
            for response_part in data:
                if isinstance(response_part, tuple):
                    #instead of beautiful soup, use regex
                    part = response_part[1].decode('utf-8')
                    msg = email.message_from_string(part)
                    email_body = quopri.decodestring(response_part[1])
                    links = re.findall(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?',email_body)
                    #file.write(email_body)
                    print(msg['Subject'])
                    for link in links:
                        concat = link[0]+"://"+link[1]+link[2]
                        file.write(concat)
                        file.write('\n')
                   #  decoded = BeautifulSoup(response_part[1], 'html.parser')
                    #file.write(response_part[1])

    except Exception, e:
        print str(e)

if __name__ == "__main__":
    with open('credentials/credentials.txt') as f:
        credentials = [x.strip().split(':', 1) for x in f]
    FROM_EMAIL = credentials[0][0]
    FROM_PWD = credentials[0][1]
    read_email_from_gmail()
