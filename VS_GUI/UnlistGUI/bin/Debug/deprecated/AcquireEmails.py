import sys
import email
import imaplib
import mailbox

"""
To enable IMAP in Gmail:
Sign in to Gmail.
Click the gear icon  in the upper-right and select Gmail settings at the top of any Gmail page.
Click Forwarding and POP/IMAP.
Select Enable IMAP.
Configure your IMAP client and click Save Changes.
"""

# Read in the login information from the user
def getLogin():
    """ Retrieve the login information for the user
    Returns:
        email - the email of the user
        password - the password of the user
    """
    file = open("credentials.txt", "r")
    email = file.readline().rstrip()
    password = file.readline().rstrip()
    return email, password


# Write out all of the senders to a text file
# Write out the emails to emails.txt
def writeEmails(email_senders):
    """Write out a list of email senders to a text file.
    Args:
        email_senders - the list of email sender names
    """
    file = open("emails.txt", "w")
    for name in email_senders:
        file.write(name)
        file.write('\n')
    file.close()


# Main method to acquire the emails
if __name__ == "__main__":

    try:
        EMAIL_ACCOUNT, PASSWORD = getLogin()
    except:
        print(" [ERROR] Unable to open <credentials.txt>")
        sys.exit(1)

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "ALL") # (ALL/UNSEEN)
    i = len(data[0].split())

    emails = set()
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        emails.add(emails_from)
    writeEmails(emails)
