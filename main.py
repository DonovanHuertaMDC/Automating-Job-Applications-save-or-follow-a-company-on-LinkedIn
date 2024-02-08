import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
from collections import OrderedDict

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
jobs = True
x = 0
scroll_attempts = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3809040764&geoId=106262181&keywords=Python%20developer%20jr.&location=M%C3%A9xico%2C%20M%C3%A9xico&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

def save():
    save_one = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
    time.sleep(5)
    if save_one.text == "Guardar":
        save_one.click()
        print("Save")
    else:
        print("Already saved")

#Select log in
try:
    log_in_linkedin = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
    log_in_linkedin.click()
except selenium.common.exceptions.NoSuchElementException:
    pass

try:
    time.sleep(5)
    type_email = driver.find_element(By.NAME, 'session_key')
    type_email.send_keys(email)
    type_password = driver.find_element(By.ID, 'password')
    type_password.send_keys(password)
    log_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    log_in.click()
except selenium.common.exceptions.ElementNotInteractableException:
    time.sleep(5)
    type_email = driver.find_element(By.NAME, 'email-or-phone')
    type_email.send_keys(email)
    type_password = driver.find_element(By.ID, 'password')
    type_password.send_keys(password)
    log_in = driver.find_element(By.XPATH, '//*[@id="join-form-submit"]')
    log_in.click()

input("Press Enter when you have solved the Captcha")

while jobs:
    a_tag_list_id = []
    time.sleep(5)
    ul_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/ul')
    a_element = ul_element.find_elements(By.TAG_NAME, 'a')

    for i in a_element:
        a_tag_list_id.append(i.get_attribute("id"))

    #print(a_tag_list_id)
    a_tag_list_id = list(OrderedDict.fromkeys(a_tag_list_id))
    max_scroll_attempts = len(a_tag_list_id)
    print(a_tag_list_id)
    print(a_tag_list_id[x::])
    print(f"max attempts: {max_scroll_attempts}")
    print(f"List ID: {len(a_tag_list_id)}")

    if len(a_tag_list_id[x::]) != 0:
        print(a_tag_list_id[x::][0])
        print(x)
        element = driver.find_element(By.XPATH, f'//*[@id="{a_tag_list_id[x::][0]}"]')

        try:
            element.click()
            time.sleep(5)
            save()
            x += 1
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("There was an exception.")
            driver.refresh()
            time.sleep(10)

    else:
        print("We've saved everything")

    try:
        left_section = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div')
        driver.execute_script("arguments[0].scrollTop += 150;", left_section)
        time.sleep(5)
        scroll_attempts += 1
    except Exception as e:
        print(f"Error during scroll: {e}")

    if scroll_attempts >= max_scroll_attempts:
        print("Reached maximum scroll attempts. Exiting loop.")
        break