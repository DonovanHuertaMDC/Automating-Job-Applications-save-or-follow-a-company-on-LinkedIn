import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import os
from dotenv import load_dotenv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import OrderedDict
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

'''email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")'''

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#driver.get("https://www.linkedin.com/")
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3809040764&geoId=106262181&keywords=Python%20developer%20jr.&location=M%C3%A9xico%2C%20M%C3%A9xico&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

#Select log in
try:
    log_in_linkedin = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
    log_in_linkedin.click()
except selenium.common.exceptions.NoSuchElementException:
    pass

#Log in 1
'''type_email = driver.find_element(By.ID, 'session_key')
type_email.send_keys(email)
type_password = driver.find_element(By.ID, 'session_password')
type_password.send_keys(password)
log_in = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
log_in.click()
time.sleep(30)'''

#Log in 2
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


#Upload your cv
'''me = driver.find_element(By.ID, 'ember13')
me.click()
settings_privacy = driver.find_element(By.ID, 'ember15')
settings_privacy.click()
data_privacy = driver.find_element(By.CSS_SELECTOR, '#PRIVACY p')
data_privacy.click()
time.sleep(5)
request_configuration = driver.find_element(By.CLASS_NAME, '#category-text__name sans-medium  ')
request_configuration.click()'''

#Find jobs
'''try:
    click_for_search_something = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
    click_for_search_something.click()

except selenium.common.exceptions.ElementNotInteractableException:
    click_for_search_something = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/button')
    click_for_search_something.click()

click_for_search_something.send_keys("Python developer jr.", Keys.ENTER)
time.sleep(10)

job_button = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
job_button.click()
time.sleep(5)'''

#City or country
'''city_country = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/div[2]')
city_country.click()
driver.execute_script("arguments[0].value = '';", city_country)'''
'''city_country_typing = driver.find_element(By.XPATH, '//*[@id="location-typeahead-instance-ember562"]/div/input[2]')
time.sleep(5)
city_country_typing.clear()
city_country.send_keys("México, México", Keys.ENTER)
apply_for_job '''

#Filters
'''add_all_filters = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/div/div')
add_all_filters.click()
results = driver.find_element(By.XPATH, '//*[@id="ember663"]')
results.click()'''

#time.sleep(5)


#Save job offer and follow company
#def save_and_follow():
'''time.sleep(5)
#Software engineer job offer
save_one = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
#time.sleep(5)
follow = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/section/section/div[1]/div[1]/button/span')
if save_one.text == "Guardar" and follow.text == "Seguir":
    follow.click()
    time.sleep(5)
    save_one.click()
elif save_one.text == "Guardar" and follow.text != "Seguir":
    save_one.click()
    print("Followed")
elif save_one.text != "Guardar" and follow.text == "Seguir":
    print("Saved")
    follow.click()
else:
    print("Saved")
    print("Followed")
    #pass'''

def save():
    #time.sleep(5)
    #Software engineer job offer
    save_one = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
    time.sleep(5)
    if save_one.text == "Guardar":
        #time.sleep(5)
        save_one.click()
        print("Save")
    else:
        print("Already saved")
        #pass

jobs = True
x = 0
#max_scroll_attempts = 10
scroll_attempts = 0


while jobs:
    a_tag_list_id = []
    time.sleep(5)
    '''employ = driver.find_element(By.CSS_SELECTOR, '#ember186')
    employ.click()'''
    #ul_element = driver.find_elements(By.XPATH, 'scaffold-layout__list-container')
    ul_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/ul')
    #time.sleep(5)
    a_element = ul_element.find_elements(By.TAG_NAME, 'a')
    #time.sleep(5)
    #print(f"hello {a_tag_list_id}")

    #The list is duplicating
    for i in a_element:
        #print(i.tag_name)
        a_tag_list_id.append(i.get_attribute("id"))

    #print(a_tag_list_id)
    a_tag_list_id = list(OrderedDict.fromkeys(a_tag_list_id))
    print(a_tag_list_id)
    print(a_tag_list_id[x::])
    max_scroll_attempts = len(a_tag_list_id)
    print(f"max attempts: {max_scroll_attempts}")
    print(f"List ID: {len(a_tag_list_id)}")

    '''for n in range(len(a_tag_list_id)):
        #time.sleep(5)
        print(a_tag_list_id[n])
        element = driver.find_element(By.XPATH, f'//*[@id="{a_tag_list_id[n]}"]')
        #'//*[@id="ember395"]'
        time.sleep(5)
        element.click()
        #time.sleep(5)
        save_and_follow()'''

    if len(a_tag_list_id[x::]) != 0:
        # time.sleep(5)
        print(a_tag_list_id[x::][0])
        print(x)
        #element = driver.find_element(By.XPATH, f'//*[@id="{a_tag_list_id[x::][x]}"]')
        element = driver.find_element(By.XPATH, f'//*[@id="{a_tag_list_id[x::][0]}"]')
        # '//*[@id="ember395"]'
        #time.sleep(5)
        try:
            element.click()
            time.sleep(5)
            save()
            x += 1
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("There was an exception.")
            driver.refresh()
            time.sleep(10)
            #a_tag_list_id.clear()
            #driver.refresh()
            #x += 1
    else:
        print("We've saved everything")
        #break
    try:
        left_section = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div')  # Ajusta el selector
        driver.execute_script("arguments[0].scrollTop += 200;", left_section)
        time.sleep(5)  # Espera adicional después del scroll para cargar los elementos
        scroll_attempts += 1
    except Exception as e:
        print(f"Error during scroll: {e}")

    if scroll_attempts >= max_scroll_attempts:
        print("Reached maximum scroll attempts. Exiting loop.")
        break