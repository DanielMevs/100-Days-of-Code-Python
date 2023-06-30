from bs4 import BeautifulSoup
import requests
from helper_functions import get_stats
import pandas as pd


boxers = ['Tyson Fury', 'Dmitry Bivol',
           'Terence Crawford',
           'Gervonta Davis']

boxer_stats = []


for boxer in boxers:
    boxer = boxer.lower().replace(' ', '-')
    response = requests.get(f'https://box.live/boxers/{boxer}/')
    boxrec_page = response.text

    soup = BeautifulSoup(boxrec_page, "html.parser")
    stats = get_stats(soup)
    
    boxer_stats.append(stats)

df = pd.DataFrame(boxer_stats)
df.to_csv('boxer_stats.csv')

