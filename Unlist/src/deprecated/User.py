class User(object):

    def __init__(gmail, password):
        if ((gmail is None) or (password is None)):
            raise Exception("ERROR: <argument has NULL value>")
        if not isGmail(gmail):
            raise Exception("ERROR: <email is not gmail>")
        self.gmail = gmail
        self.password = password

    def isGmail(email_address):
        substr = "@gmail.com"
        if (substr in email_address):
            return True
        else:
            return False

    def getGmail():
        return self.gmail

    def getPassword():
        return self.pasword
