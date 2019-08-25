from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import time
import sys
import os
NEXT_BUTTON = "//div[@class='h0']/div[2]"
BACK_BUTTON = "//div[@class='h0']/div[1]"
# Keep looping until the next one is reached
def reachNextElement(i):

    # If 50 is reached, wait to allow Chrome to load more
    if (i == 50):
        time.sleep(5)

    # Try to reach next email
    stale_element = True
    while (stale_element):
        try:
            time.sleep(0.1)
            driver.find_element_by_xpath(NEXT_BUTTON).click()
            stale_element = False
        except StaleElementReferenceException:
            stale_element = True
        except ElementClickInterceptedException:
            stale_element = True
def goBack(i):

    # Try to reach previous email
    stale_element = True
    while (stale_element):
        try:
            time.sleep(0.1)
            driver.find_element_by_xpath(BACK_BUTTON).click()
            stale_element = False
        except StaleElementReferenceException:
            stale_element = True
        except ElementClickInterceptedException:
            stale_element = True

def clickUnsubscribe(i):

    # If 50 is reached, wait to allow Chrome to load more
    if (i == 50):
        time.sleep(5)

    # Try to reach next email
    stale_element = True
    while (stale_element):
        try:
            time.sleep(0.1)
            driver.find_element_by_xpath("//*[contains(text(), 'Unsubscribe')]").click()
            stale_element = False
        except StaleElementReferenceException:
            stale_element = True
        except ElementClickInterceptedException:
            stale_element = True

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

#Driver for logging into Gmail, and unsubscribing from selected emails.
if __name__ == "__main__":

    # Define constants: login link and the path to the chromedriver.exe file
    GMAIL_LOGIN = "https://accounts.google.com/ServiceLogin?service=mail"
    CHROMEDRIVER_PATH = os.getcwd()
    GMAIL, PASSWORD = getLogin()
    TRACEBACK = "\n [LOGGING] Clean exit... goodbye"

    try:
        # Run the window without it being open
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        ######################################

        # Asssumes that chromedriver.exe is placed in the current working directory
        driver = webdriver.Chrome(CHROMEDRIVER_PATH + "/chromedriver.exe")
        time.sleep(1)

        # Tell the driver to open up the webpage
        driver.get(GMAIL_LOGIN)
        #driver.minimize_window()

        border = " ===================================================================="
        print(border)
        print(" ==== PROGRAM ACTIVE, DO NOT USE WINDOW UNTIL PROGRAM COMPLETION ====")
        print(border + '\n')

        # Send the email to the login page
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(GMAIL)
        driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        time.sleep(1)

        # Send the password to the login page
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(PASSWORD)
        driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        time.sleep(1)


        email_count = driver.find_element_by_xpath("//span[@class='Dj']/span[2]").text
        email_count = int(email_count)
        print(" [LOGGING] Found", email_count, "emails!")

        # Load up all of the emails
        driver.implicitly_wait(5)
        emails = driver.find_elements_by_xpath("//*[@class='yW']/span")

        # Access the first email
        if email_count > 0:
            driver.implicitly_wait(5)
            emails[0].click()
        with open("selected_emails.txt") as f:
            selected_emails = f.readlines()
        selected_emails = [x.strip() for x in selected_emails]
        print(selected_emails)
        # Create a dictionary to hold the emails to unsubscribe from
        email_dict = {}
        for i in range(0,email_count):

            # Find the name of the sender
            driver.implicitly_wait(5)
            sender = driver.find_element_by_xpath("//span[@class='gD']").get_attribute("name")
            print(sender)
            #print("COMPARING: ", sender, " | ", selected_emails[selected_index])
            if(sender in selected_emails):
                try:
                    driver.implicitly_wait(5)
                    if (driver.find_element_by_xpath("//*[contains(text(), 'Unsubscribe')]") != None):
                        print(" [LOGGING] Unsubscribed from \"" + sender + "\"...")
                        goBack(i)
                        selected_emails.remove(sender)
                        clickUnsubscribe(i)
                        driver.find_element_by_name("s").click()
                    else:
                        print("NOT FOUND")
                except NoSuchElementException:
                    print(" [LOGGING] \"" +sender+ "\": Already unsubscribed or unable to...")

                time.sleep(2)
            else:
                print(" [LOGGING] \"" +sender+ "\": Email not selected!")
            reachNextElement(i)

    except Exception as e:
        print("\n" + border, border, sep="\n")
        print(e)
        TRACEBACK = traceback.format_exc()

    finally:
        print(TRACEBACK)
        driver.close()
        sys.exit(0)
