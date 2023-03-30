from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_path = "C:\\Users\Dani\\Development\\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

stats = driver.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]')

print(stats.text)

# stats.click()

portal = driver.find_element(By.LINK_TEXT, 'Content portals')
portal.click()

search = driver.find_element(By.CSS_SELECTOR, '[type="search"]')
search.send_keys("Python")
search.send_keys(Keys.ENTER)
driver.quit()