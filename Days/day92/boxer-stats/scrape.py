from bs4 import BeautifulSoup
import requests

boxers = ['Oleksandr Usyk', 'Tyson Fury', 'Dmitry Bivol', 'Canelo Alvarez',
           'Terence Crawford', 'Errol Spence Jr.', 'Teofimo Lopez', 
           'Devin Haney', 'Gervonta Davis', 'Naoya Inoue']
response = requests.get('https://box.live/boxers/naoya-inoue/')
# print(response.text)
boxrec_page = response.text

soup = BeautifulSoup(boxrec_page, "html.parser")
name = soup.title.get_text().split('-')[0]
print(f'Boxer name: {name}')
stats = soup.find_all(name="div", class_="stats-row__content text-left ml-3 headings-text-color")
for stat in stats:
    print(stat.get_text())
# height = soup.find(name="div", class_='stats-row__content text-left ml-3 headings-text-color')
# height_description = height.get_text() if height else "No Description"
# print(f'Height: {height_description}')
