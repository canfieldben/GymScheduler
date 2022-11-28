from selenium import webdriver
from twilio.rest import Client
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

timeout = 7
PATH = "C:\Program Files (x86)\chromedriver.exe"


def floor_check():
    floor = input("Enter floor (1, 2, 3, basement): ")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver_chrome = webdriver.Chrome(options=options, executable_path=PATH)
    if floor == "1":
        driver_chrome.get("https://bewell.ese.syr.edu/Program/GetProgramDetails?courseId=ddf2dc35-5cca-4e65-84b2-0ef278c6ae38&semesterId=fb963dc4-ba57-4f69-b2dd-000111fcc3d5")
    elif floor == '2':
        driver_chrome.get("https://bewell.ese.syr.edu/Program/GetProgramDetails?courseId=a408af33-b02f-4984-8a71-1af7c00974de&semesterId=fb963dc4-ba57-4f69-b2dd-000111fcc3d5")
    elif floor == "3":
        driver_chrome.get("https://bewell.ese.syr.edu/Program/GetProgramDetails?courseId=1d7fe9c7-2df9-4838-82fe-1552680ac041&semesterId=fb963dc4-ba57-4f69-b2dd-000111fcc3d5")
    elif floor == 'basement':
        driver_chrome.get(
            "https://bewell.ese.syr.edu/Program/GetProgramDetails?courseId=1c6549d3-771f-4d05-8dbb-649106ec4226&semesterId=d5f29aee-e3cf-4ba2-9367-7f026f560f08")
    else:
        print("please enter a valid input")
        floor_check()

    return driver_chrome


driver = floor_check()

logIn = driver.find_element_by_id("loginLink")
logIn.send_keys(Keys.RETURN)

element_present = EC.presence_of_element_located((By.XPATH, "//*[@title='NetID Login']"))
WebDriverWait(driver, timeout).until(element_present)

netId = driver.find_element_by_xpath("//*[@title='NetID Login']")
netId.click()

username = driver.find_element_by_id("username")
username.send_keys("becanfie")

password = driver.find_element_by_id("password")
password.send_keys("Ktm_!321")

loginEnter = driver.find_element_by_name("_eventId_proceed")
loginEnter.click()

loopBool = True

while loopBool:

    def check_exists_by_xpath():
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[1]/div/div/div[2]/button')
        except NoSuchElementException:
            return False
        return True


    def check_exists_by_xpath1():
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[2]/div/div/div[2]/button')

        except NoSuchElementException:
            return False
        return True


    def check_exists_by_xpath2():
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[3]/div/div/div[2]/button')
        except NoSuchElementException:
            return False
        return True


    def check_exists_by_xpath3():
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[4]/div/div/div[2]/button')
        except NoSuchElementException:
            return False
        return True


    #if check_exists_by_xpath():
        smsText = driver.find_element_by_xpath(
            '//*[@id="mainContent"]/div[2]/section/div[1]/div/div/div[1]/small').text[:5]

        # client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        # client.messages.create(to='+19545407256', from_='+17722665171', body='Slot 1 Open')

        client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        client.messages.create(to='+19786976468', from_='+17722665171', body=smsText + ' slot open\nSalty Inc™')

        time.sleep(10)
    if check_exists_by_xpath1():
        smsText = driver.find_element_by_xpath(
            '//*[@id="mainContent"]/div[2]/section/div[2]/div/div/div[1]/small').text[:5]

        # client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        # client.messages.create(to='+19545407256', from_='+17722665171', body='Slot 2 Open')

        client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        client.messages.create(to='+19786976468', from_='+17722665171', body=smsText + ' slot open\nSalty Inc™')

        time.sleep(10)
    if check_exists_by_xpath2():
        smsText = driver.find_element_by_xpath(
            '//*[@id="mainContent"]/div[2]/section/div[3]/div/div/div[1]/small').text[:5]

        # client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        # client.messages.create(to='+19545407256', from_='+17722665171', body='Slot 3 Open')

        client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        client.messages.create(to='+19786976468', from_='+17722665171', body=smsText + ' slot open\nSalty Inc™')

        time.sleep(10)
    if check_exists_by_xpath3():
        smsText = driver.find_element_by_xpath(
            '//*[@id="mainContent"]/div[2]/section/div[1]/div/div/div[1]/small').text[:5]

        # client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        # client.messages.create(to='+19545407256', from_='+17722665171', body='Slot 4 Open')

        client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        client.messages.create(to='+19786976468', from_='+17722665171', body=smsText + ' slot open\nSalty Inc™')

        time.sleep(10)

    driver.refresh()
    #time.sleep(1)
