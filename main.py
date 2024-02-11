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

def close_pop_up():
    time.sleep(5)
    close_pop_up = driver.find_element(By.XPATH, '//*[@id="artdeco-modal-outlet"]/div/div/button')
    close = close_pop_up.get_attribute("id")
    print(close)
    close_pop_up.click()

#Save job offer and follow company
def save_and_follow():
    time.sleep(5)
    save_one = driver.find_element(By.CSS_SELECTOR, '#main > div.scaffold-layout__list-detail-inner > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div.job-details-jobs-unified-top-card__content--two-pane > div.mt5 > div > button')
    save_job = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
    time.sleep(5)
    follow_link = driver.find_element(By.CSS_SELECTOR, '#main > div.scaffold-layout__list-detail-inner > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div.job-details-jobs-unified-top-card__content--two-pane > div.job-details-jobs-unified-top-card__primary-description-container > div > a')
    def following_company(z):
        follow = driver.find_element(By.XPATH, f'//*[@class="ember-view"]/div[2]/div[2]/div[{z}]/div/div[1]/div[1]/button')
        time.sleep(3)
        follow.click()
        print("Following")
        time.sleep(2)
        driver.back()

    if save_job.text == "Guardar":
        save_one.click()
        print("Saving")
        follow_link.click()
        time.sleep(5)
        try:
            close_pop_up()
        except selenium.common.exceptions.NoSuchElementException:
            pass

        try:
            z = 2
            follow_company = driver.find_element(By.XPATH, f'//*[@class="ember-view"]/div[2]/div[2]/div[{z}]/div/div[1]/div[1]/button/span')
            if follow_company.text == "Seguir":
                following_company(z)
            else:
                print("Already followed")
                driver.back()
        except selenium.common.exceptions.NoSuchElementException:
            z = 3
            follow_company = driver.find_element(By.XPATH, f'//*[@class="ember-view"]/div[2]/div[2]/div[{z}]/div/div[1]/div[1]/button/span')
            if follow_company.text == "Seguir":
                following_company(z)
            else:
                print("Already followed")
                driver.back()
    elif save_job.text != "Guardar":
        print("Already saved")
        follow_link.click()
        time.sleep(5)
        try:
            close_pop_up()
        except selenium.common.exceptions.NoSuchElementException:
            pass

        try:
            z = 2
            follow_company = driver.find_element(By.XPATH, f'//*[@class="ember-view"]/div[2]/div[2]/div[{z}]/div/div[1]/div[1]/button/span')
            if follow_company.text == "Seguir":
                following_company(z)
            else:
                print("Already followed")
                driver.back()
        except selenium.common.exceptions.NoSuchElementException:
            z = 3
            follow_company = driver.find_element(By.XPATH, f'//*[@class="ember-view"]/div[2]/div[2]/div[{z}]/div/div[1]/div[1]/button/span')
            if follow_company.text == "Seguir":
                following_company(z)
            else:
                print("Already followed")
                driver.back()

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
    time.sleep(5)
    log_in_direct = driver.find_element(By.CSS_SELECTOR, '#main-content > div > form > p > button')
    log_in_direct.click()

#log in
try:
    time.sleep(5)
    type_email = driver.find_element(By.NAME, 'session_key')
    type_email.send_keys(email)
    type_password = driver.find_element(By.ID, 'password')
    type_password.send_keys(password)
    log_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    log_in.click()
except selenium.common.exceptions.ElementNotInteractableException:
    driver.refresh()
    time.sleep(5)
    type_email = driver.find_element(By.NAME, 'session_key')
    type_email.send_keys(email)
    type_password = driver.find_element(By.ID, 'session_password')
    type_password.send_keys(password)
    log_in = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/form/div[2]/button')
    log_in.click()

#Python jr developer job offers
input("Press Enter when you have solved the Captcha")
time.sleep(5)

while jobs:
    a_tag_list_id = []
    #time.sleep(5)
    ul_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/ul')
    a_element = ul_element.find_elements(By.TAG_NAME, 'a')

    for i in a_element:
        a_tag_list_id.append(i.get_attribute("id"))

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
            #save()
            save_and_follow()
            x += 1
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("There was an exception.")
            driver.refresh()
            time.sleep(10)
            # save()
            save_and_follow()
            x += 1
    else:
        print("We've saved everything")

    try:
        left_section = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div')
        driver.execute_script("arguments[0].scrollTop += 250;", left_section)
        time.sleep(5)
        scroll_attempts += 1
    except Exception as e:
        print(f"Error during scroll: {e}")

    if scroll_attempts >= max_scroll_attempts:
        print("Reached maximum scroll attempts. Exiting loop.")
        time.sleep(5)
        driver.quit()
        break