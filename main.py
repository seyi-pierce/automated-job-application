from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

USER_NAME = input("Please enter your email address")
PASSWORD_ = input("Please enter your password")
chrome_driver_path = "C:/Users/19402/Applications/chromedriver"
job_app_url ="https://www.linkedin.com/jobs/search/?f_AL=true&geoId=105365761&keywords=software%20engineer&location=" \
             "Nigeria"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(job_app_url)

sign_in = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")
sign_in.click()

time.sleep(5)

username = driver.find_element(by=By.ID, value="username")
username.send_keys(USER_NAME)
password = driver.find_element(by=By.ID, value="password")
password.send_keys(PASSWORD_)
final_sign_in = driver.find_element(by=By.CLASS_NAME, value="from__button--floating")
final_sign_in.click()

job_listings = driver.find_elements(by=By.CLASS_NAME, value="job-flavors__flavor")

for job in job_listings:
    print("Application in Progress")
    job.click()
    time.sleep(2)
    try:
        click_easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button").click()
        phone_number = driver.find_element(by=By.NAME, value='urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:'
                                                     '3091967508,56460658,phoneNumber~nationalNumber)')
        if phone_number == "":
            phone_number.send_keys("8122277570")

        submit_button = driver.find_elements(by=By.CSS_SELECTOR, value="div form footer div .artdeco-button--primary")[-1]
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    except NoSuchElementException:
        print("Application not found!")
        continue

time.sleep(5)
driver.quit()

