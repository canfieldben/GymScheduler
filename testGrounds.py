import ctypes
import time
from twilio.rest import Client
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process


def main(name, username, password, user_time):
    print(username)
    print(password)
    print(user_time)
    PATH = 'C:\\Users\\Ben\\PycharmProjects\\gymScript\\driver\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    driver.maximize_window()
    timeout = 15

    def statement_check(slot_name, position):
        if position == 1:
            print(slot_name + " time True")
        if position == 2:
            print(slot_name + " button True")

    def check_slot_one():
        print("Checking slot 1...")
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[1]/div/div/div[2]/button')
        except NoSuchElementException:
            return False
        return True

    def check_slot_two():
        print("Checking slot 2...")
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[2]/div/div/div[2]/button')
        except NoSuchElementException:
            return False
        return True

    def check_slot_three():
        print("Checking slot 3...")
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[3]/div/div/div[2]/button')
        except NoSuchElementException:
            return False
        return True

    def check_slot_four():
        print("Checking slot 4...")
        try:
            driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/section/div[4]/div/div/div[2]/button')
        except NoSuchElementException:
            return False
        return True

    def initial_opening(username1, password1):
        driver.get(
            'https://bewell.ese.syr.edu/Program/GetProgramDetails?courseId=1c6549d3-771f-4d05-8dbb-649106ec4226&semesterId=d5f29aee-e3cf-4ba2-9367-7f026f560f08')
        logIn = driver.find_element_by_id("loginLink")
        logIn.send_keys(Keys.RETURN)

        element_present = EC.presence_of_element_located((By.XPATH, "//*[@title='NetID Login']"))
        WebDriverWait(driver, timeout).until(element_present)
        netId = driver.find_element_by_xpath("//*[@title='NetID Login']")
        driver.execute_script("arguments[0].click();", netId)

        username_button = driver.find_element_by_id("username")
        username_button.send_keys(username1)
        password_button = driver.find_element_by_id("password")
        password_button.send_keys(password1)

        loginEnter = driver.find_element_by_name("_eventId_proceed")
        driver.execute_script("arguments[0].click();", loginEnter)


    def button_check(user_time):
        pop_up = ""
        button_loaded = False
        testBool1 = True
        testBool2 = False
        testBool3 = False
        testBool4 = False
        while not button_loaded:
            driver.refresh()
            time.sleep(.5)
            if time.strftime("%H%M") == "0030" or testBool1:
                statement_check("slot 1", 1)
                if check_slot_one():
                    statement_check("slot 1", 2)
                    pop_up = sign_up('//*[@id="mainContent"]/div[2]/section/div[1]/div/div/div[2]/button')
                    button_loaded = True
            if time.strftime("%H%M") == "0230" or testBool2:
                statement_check("slot 2", 1)
                if check_slot_two():
                    statement_check("slot 2", 2)
                    pop_up = sign_up('//*[@id="mainContent"]/div[2]/section/div[2]/div/div/div[2]/button')
                    button_loaded = True
            if time.strftime("%H%M") == "0430" or testBool3:
                statement_check("slot 3", 1)
                if check_slot_three():
                    statement_check("slot 3", 2)
                    pop_up = sign_up('//*[@id="mainContent"]/div[2]/section/div[3]/div/div/div[2]/button')
                    button_loaded = True
            if time.strftime("%H%M") == "0830" or time.strftime(
                    "%H%M") == "1030" or time.strftime("%H%M") == "1230" or time.strftime(
                    "%H%M") == "1430" or time.strftime(
                    "%H%M") == "0630" or testBool4:
                statement_check("slot 4", 1)
                if check_slot_four():
                    statement_check("slot 4", 2)
                    pop_up = sign_up('//*[@id="mainContent"]/div[2]/section/div[4]/div/div/div[2]/button')
                    button_loaded = True

        return pop_up

    def sign_up(time_slot):
        regButton = driver.find_element_by_xpath(time_slot)
        driver.execute_script("arguments[0].click();", regButton)

        element_present = EC.presence_of_element_located((By.ID, "btnAccept"))
        WebDriverWait(driver, timeout).until(element_present)
        accWaiver = driver.find_element_by_id("btnAccept")
        driver.execute_script("arguments[0].click();", accWaiver)

        element_present = EC.presence_of_element_located((By.ID, "checkoutButton"))
        WebDriverWait(driver, timeout).until(element_present)
        checkOut = driver.find_element_by_id("checkoutButton")
        checkOut.click()

        smsText = driver.find_element_by_xpath(
            '//*[@id="ShoppingCartItems"]/div[2]/table/tbody/tr/td[1]/small').text[34:]

        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="CheckoutModal"]/div/div[2]/button[2]'))
        WebDriverWait(driver, timeout).until(element_present)
        finalCheck = driver.find_element_by_xpath('//*[@id="CheckoutModal"]/div/div[2]/button[2]')
        driver.execute_script("arguments[0].click();", finalCheck)

        client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        client.messages.create(to='+19786976468', from_='+19782952654',
                               body="{} booked for: {}\nSalty Inc™".format(smsText, name))

        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="ShoppingCartItems"]/div[2]/table/tbody/tr/td[6]/span/span/a'))
        WebDriverWait(driver, timeout).until(element_present)

        client = Client("AC47a6ff00aab2bd47aad2b12b3a3705bb", '7ee00f633161e65a93b36b502f9a11e7')
        client.messages.create(to='+19786976468', from_='+19782952654',
                               body="{} booked for: {}\nSalty Inc™".format(smsText, name))

        return smsText

    initial_opening(username, password)
    sms_text = button_check(user_time)
    driver.minimize_window()
    ctypes.windll.user32.MessageBoxW(0, sms_text, "Salty Inc™", 1)
    driver.quit()


class Users:

    def __init__(self, name, username, password, user_time):
        self.name = name
        self.username = username
        self.password = password
        self.time = user_time


with open("restricted.txt") as file:
    user_list = []
    inputs = file.readlines()
    count = 0
    for i in inputs:
        temp_list = i.split(" ")
        if (temp_list[3].strip() == "0") or (
                temp_list[0] != "#" and int(temp_list[3].strip()) - 1 == int(time.strftime("%H%M"))):
            name1 = Users(temp_list[0].strip(), temp_list[1].strip(), temp_list[2].strip(), temp_list[3].strip())
            user_list.append(name1)

if __name__ == '__main__':
    for i in user_list:
        time.sleep(.1)
        p1 = Process(target=main, args=(i.name, i.username, i.password, i.time))
        p1.start()
