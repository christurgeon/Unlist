from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import traceback
import time
import sys
import os

# unlist.rcos@gmail.com
# RCOS_unlist!

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


# Read in the login information from the user
def getLogin():
    file = open("credentials.txt", "r")
    email = file.readline().rstrip()
    password = file.readline().rstrip()
    return email, password


if __name__ == "__main__":

    # Define constants: login link and the path to the chromedriver.exe file
    GMAIL_LOGIN = "https://accounts.google.com/ServiceLogin?service=mail"
    CHROMEDRIVER_PATH = os.getcwd()
    GMAIL, PASSWORD = getLogin()
    tb = ""

    try:
        # Asssumes that chromedriver.exe is placed in the current working directory
        driver = webdriver.Chrome(CHROMEDRIVER_PATH + "/driver.exe")
        driver.implicitly_wait(5)

        # Tell the driver to open up the webpage
        driver.get(GMAIL_LOGIN)
        time.sleep(1)

        # Send the email to the login page
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(GMAIL)
        driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        time.sleep(1)

        # Send the password to the login page
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(PASSWORD)
        driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        time.sleep(1)

        # Accept automated browsing --- this still needs to be tested
        """
        try:
            driver.find_element_by_xpath('//*[@id="identifierDone"]').click()
        except:
            print("Did not prompt user to accept automated browsing...")
        try:
            driver.find_element_by_xpath("//div[@role='link']").click()
        except:
            print("Did not prompt user for confirm email...")
        """

        # Load up all of the emails
        emails = driver.find_elements_by_xpath("//*[@class='yW']/span")
        driver.implicitly_wait(5)

        # Get the names from all of the emails
        names = [email.text for email in emails]
        print("Found", len(emails), "emails!")

        # Access the first email
        if len(emails) > 0:
            emails[0].click()
            driver.implicitly_wait(5)

        # Create a dictionary to hold email sender names that have been found
        #         KEY: sender (string)
        #       VALUE: unsubscribe link (string)
        # value is empty string "" if no link found
        email_dict = {}
        for i in range(len(emails)):
            sender = names[i]

            # Continue if an unsubscribe link has already been found
            if sender in email_dict:
                print("Already processed " + sender + "...")
                continue

            # If a new email is found, see if we can unsubscribe from it
            if sender not in email_dict:
                driver.implicitly_wait(5)
                try:
                    if (driver.find_element_by_class_name("Ca") != None):
                        print("Can unsubscribe from " + sender + "...")
                        email_dict[sender] = 1
                except NoSuchElementException:
                    print(sender + ": Already unsubscribed or unable to...")
                    driver.implicitly_wait(2)

                # Click the next email button
                next = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji adg T-I-awG T-I-ax7 T-I-Js-Gs L3']")
                driver.implicitly_wait(5)
                continue

        writeEmails(email_dict)
    except Exception as e:
        print(e)
        tb = traceback.format_exc()
    finally:
        print(tb)
        #driver.close()
        sys.exit(0)
