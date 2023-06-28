from bs4 import BeautifulSoup as btfl_sp


def get_name(soup: btfl_sp) -> str:
    return soup.title.get_text().split('-')[0].rstrip()

def get_weight_class(soup: btfl_sp) -> str:
    weight_class = soup.find_all(name="h4", class_="single-fight__title text-center")
    return weight_class[-1].get_text().split('@')[-1].lstrip()

def get_stats(soup: btfl_sp) -> dict:
    stats = {
        'name': '',
        'weightClass': '',
        'age': '',
        'height': '',
        'reach': '',
        'stance': '',
        'wins': '',
        'winsByKO': '',
        'KO%': '',
        'lost': '',
        'stopped': '',
        'draws': '',
        'debut': '',
        'proRounds': '',
        'Ring-Rank': '',
        'WBO-Rank': '',
        'IBF-Rank': '',
        'WBC-Rank': '',
        'WBA-Rank': '',

    }
    stat_scrape = soup.find_all(name="div", class_="stats-row__content text-left ml-3 headings-text-color")

    i = 9
    for key in stats.keys():
        if key == 'name':
            stats['name'] = get_name(soup)
        elif key == 'weightClass':
            stats['weightClass'] = get_weight_class(soup)

        else:
            stats[key] = stat_scrape[i].get_text().replace(
                '\n', '').replace("\'", "'").strip()

            i += 1
    return stats
