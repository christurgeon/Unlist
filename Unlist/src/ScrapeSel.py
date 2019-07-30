from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os
#Driver for logging into Gmail, and unsubscribing from selected emails.
if __name__ == "__main__":
    login_url = "https://accounts.google.com/ServiceLogin?service=mail"
    driver_path = os.getcwd()
    USER = "unlist.rcos@gmail.com"
    PASS = "RCOS_unlist!"
    driver = webdriver.Chrome(driver_path+"/chromedriver.exe")
    
    driver.get(login_url)
    driver.find_element_by_id("identifierId").send_keys(USER)
    driver.find_element_by_id("identifierNext").click()

    driver.implicitly_wait(2)
    driver.find_element_by_name('password').send_keys(PASS)
    driver.find_element_by_id("passwordNext").click()
   # driver.find_element_by_xpath('//button[@id="passwordNext"]')
    time.sleep(1)
    with open("selected_emails.txt") as f:
        selected_emails = f.readlines()
    selected_emails = [x.strip() for x in selected_emails] 
    print(selected_emails)
    emails = []
    selected_index = 0
    emails = driver.find_elements_by_xpath("//*[@class='yW']/span")
    for i in range(len(emails)):
        emails = driver.find_elements_by_xpath("//*[@class='yW']/span")
        time.sleep(1)
        if(emails[i].text == selected_emails[selected_index]):
            selected_index += 1
            emails[i].click()
            time.sleep(2)
            try:
                driver.find_element_by_class_name("Ca").click()
            except NoSuchElementException:
                driver.execute_script("window.history.go(-1)")
                time.sleep(1)
                continue
            time.sleep(1)
            driver.find_element_by_name("s").click()
            time.sleep(1)
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
            
            if(selected_index == len(selected_emails)):
                break

   # driver.close()

    