from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_path = "your chrome path"

driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://www.python.org/')

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
date_items = [date.text.split('\n')[0] for date in dates]
# print(date_items)

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_items = [event.text for event in events]
# print(event_items)

event_dict = [{'event': event, 'date': date} for event, date in list(zip(event_items, date_items))]

final_dict = {}

for idx, item in enumerate(event_dict):
    final_dict.update({idx: item})

print(final_dict)

