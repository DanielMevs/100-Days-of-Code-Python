from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_path = "C:\\Users\Dani\\Development\\chromedriver"
import time

driver = webdriver.Chrome(executable_path=chrome_path)

PHONE_NUMBER = 'MY_NUMBER'
EMAIL = 'MY_EMAIL'
PASSWORD = 'MY_PASSWORD'

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3557884837&f_AL=true&keywords=python%20developer&refresh=true")

driver.find_element(By.CSS_SELECTOR, '.nav__button-secondary').click()

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

username.send_keys(EMAIL)
password.send_keys(PASSWORD)

driver.find_element(By.CSS_SELECTOR, '.btn__primary--large').click()
time.sleep(10)

jobs = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
job_titles = [title.text for title in driver.find_elements(By.CSS_SELECTOR, '[class="disabled ember-view job-card-container__link job-card-list__title"]')]
job_companies = [company.text for company in driver.find_elements(By.CSS_SELECTOR, '[class="job-card-container__primary-description "]')]
print('Job titles: ', job_titles)
print('Job companyies: ', job_companies)
jobs_info = list(zip(job_titles, job_companies))


def cancel_application():
    cancel_icon = driver.find_element(By.CSS_SELECTOR, '[type="cancel-icon"]')
    cancel_icon.click()

    discard_btn = driver.find_element(By.CSS_SELECTOR, '[data-control-name="discard_application_confirm_btn"]')
    discard_btn.click()

for job in jobs:
    if not jobs_info:
        break
    job.click()
    time.sleep(3)

    title, company = jobs_info.pop(0)
    label = f'Apply to {title} at {company}'

    print('Label: ', label)

    easy_apply = driver.find_element(By.CSS_SELECTOR, f'[aria-label="{label}"]')
    # easy_apply = driver.find_element(By.CSS_SELECTOR, '[class="jobs-apply-button"]')
    easy_apply.click()

    time.sleep(5)

    inputs = driver.find_elements(By.CSS_SELECTOR, 'input')[:5]

    for input in inputs:
        if input.get_attribute('type') == 'text' and not input.text:
            input.send_keys(PHONE_NUMBER)





    