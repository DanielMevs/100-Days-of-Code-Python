from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_path = "C:\\Users\Dani\\Development\\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_path)

driver.get("https://www.amazon.com/dp/B0B4PQDFCL/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t")

price = driver.find_element(By.CLASS_NAME, "a-price")
print('price: ', price.text.replace('\n', '.'))
print('tag name: ', price.tag_name)

other_element = driver.find_element(By.ID, "corePriceDisplay_desktop_feature_div")
print('attribute value for data-feature-name: ', other_element.get_attribute("data-feature-name"))

logo = driver.find_element(By.CLASS_NAME, "nav-logo-link")
print('Logo size: ', str(logo.size))

# driver.close()
# driver.quit()

driver.get('https://www.python.org/')

docs_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
print('docs link: ', docs_link.get_attribute('href'))

driver.quit()
