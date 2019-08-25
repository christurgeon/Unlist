from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
from bs4 import BeautifulSoup
from flask import Flask
from urllib import parse
import quopri
import base64
import email
import pickle
import os.path
import json


# =============================================================================
# =============================================================================


def GetMessageWithId(service, user_id, msg_id, format):
    """Get a Message with given ID.
    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        msg_id: The ID of the Message required.
    Returns:
        A Message.
    """
    try:
        message = service.users().messages().get(userId=user_id,
                                                 id=msg_id,
                                                 format=format).execute()
        msg_str = str(base64.urlsafe_b64decode(message["raw"].encode("utf-8")))
        return msg_str
    except errors.HttpError as error:
        print("An error occurred: %s" % error)


# =============================================================================
# =============================================================================


def ListMessagesWithLabels(service, user_id, label_ids=[]):
  """List all Messages of the user's mailbox with label_ids applied.
  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_ids: Only return Messages with these labelIds applied.
  Returns:
    List of Messages that have all required Labels applied. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate id to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               labelIds=label_ids).execute()
    messages = []
    if "messages" in response:
      messages.extend(response["messages"])

    while 'nextPageToken' in response:
      page_token = response["nextPageToken"]
      response = service.users().messages().list(userId=user_id,
                                                 labelIds=label_ids,
                                                 pageToken=page_token).execute()
      messages.extend(response["messages"])
    return messages
  except errors.HttpError as error:
      print("An error occurred: %s" % error)


# =============================================================================
# =============================================================================


def BatchDelete(service, user_id, ids_list):
    """Delete a Message.
    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        msg_id: ID of Message to delete.
    """
    for msg_id in ids_list:
        try:
            service.users().messages().delete(userId=user_id, id=msg_id).execute()
        except errors.HttpError as error:
            print("An error occurred trying to delete %d" % msg_id)
            print("ERROR: %s", error)


# =============================================================================
# =============================================================================


def FilterRawEmail(raw_msg):
    """Create a list of all href links in an email.
    Args:
        raw_msg: Raw message used to beautify with BeautifulSoup
    Returns:
        List of https links found from the email message
    """
    links = []
    soup = BeautifulSoup(raw_msg, features="lxml")
    for a_tag in soup.find_all("a", href=True):
        link = a_tag["href"]
        if (len(link) < 10):
            continue
        else:
            print("Before Cleaning:  ", link, end="\n\n")
            clean_link = parse.unquote_plus(quopri.decodestring(link).decode('utf-8'))
            print("Link:  ", clean_link, end = "\n\n")
            links.append(clean_link)
    return links


# =============================================================================
# =============================================================================


    def WriteToFile(msg, file_name):
        """Write out a message to a file for debugging purposes.
            Args:
                msg: a message object
                file_name: the output file name
            Returns:
                None
        """
        out_msg = str(msg)
        file = open(file_name, "w")
        file.write(str(decoded_msg))


# =============================================================================
# =============================================================================


def configure(SCOPES, CREDENTIALS_PATH):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    service = build("gmail", "v1", credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
        print("No labels found.")
    else:
        print("Labels:")
        for label in labels:
            print(label["name"])
    return service


# =============================================================================
# =============================================================================


if __name__ == "__main__":

    GMAIL = "unlist.RCOS@gmail.com"
    PASSWORD = "RCOS_unlist!"
    EMAIL_COUNT = 100

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    CREDENTIALS_PATH = "../../credentials.json"
    service = configure(SCOPES, CREDENTIALS_PATH)

    # Retrieve list of all messages
    response = service.users().messages().list(userId="me",
                                               labelIds=["INBOX"],
                                               maxResults=EMAIL_COUNT,
                                               includeSpamTrash=True).execute()

    email_count = response["resultSizeEstimate"]
    print("Found", email_count, "messages!")

    for msg in response["messages"]:
        msg_id = msg["id"]
        message = GetMessageWithId(service, "me", msg_id, "raw")
        links = FilterRawEmail(message)
