from bs4 import BeautifulSoup as btfl_sp
from bs4.element import ResultSet as rs


def get_name(soup: btfl_sp) -> str:
    return soup.title.get_text().split('-')[0].rstrip()


def find_get_stats_start_index(results: rs) -> int:
    start_idx = 0

    for stat in results:
        val = stat.get_text().strip()
        
        if len(val) == 2 and val.isnumeric():
            start_idx = results.index(stat)
            break

    return start_idx


def is_weight_class_accessible(results: rs) -> bool:
    has_weight_class = False

    for result in results:
        val = result.get_text().strip()
        if 'weight' in val.lower():
            return True
    
    return False


def find_get_weight_class_start_index(results: rs) -> int:
    
    start_idx = 0
    
    for stat in results:
        val = stat.get_text().strip()
        
        if 'weight' in val.lower():
            start_idx = results.index(stat)
            has_weight_class = True
            break

    return start_idx


def get_weight_class_alternative(soup: btfl_sp) -> str:
    weight_class_rs = soup.find_all(name="div", class_="stats-row__title w-100 headings-font-family headings-text-color text-center d-flex align-items-center justify-content-center stats-row__title--normal text-truncate")
    weight_class = ''
    weight_class_tracker = []
    
    for result in weight_class_rs:
        i = 0
        words = result.get_text().split(' ')
        for word in words:
            weight_class_temp = ''
            if 'weight' in word.lower():
                if words[i - 1].lower() == 'super':
                    weight_class_temp += words[i - 1].title()
                    weight_class_temp += ' ' + word.title()
                    if weight_class_temp not in weight_class_tracker:
                        if weight_class:
                            weight_class += ', ' + weight_class_temp
                        else:
                            weight_class += weight_class_temp
                    else:
                        continue
                else:
                    weight_class_temp += ' ' + word.title()
                    if weight_class_temp not in weight_class_tracker:
                        if weight_class:
                            weight_class += ', ' + weight_class_temp
                        else:
                            weight_class += weight_class_temp
                    else:
                        continue
            i += 1

        return weight_class
    

def get_rank(soup: btfl_sp, key: str) -> str:
    weight_class_rs = soup.find_all(name="div", class_="stats-row__title w-100 headings-font-family headings-text-color text-center d-flex align-items-center justify-content-center stats-row__title--normal text-truncate")
    organization = key.split('-')[0].lower()
    for result in weight_class_rs:
        i = 0
        belts_held = result.get_text().replace('\n', '').lower().split(' ')
        print(belts_held)
        print(organization in belts_held)
        if organization in belts_held:
            return 'C'
    
    return '-'


def get_weight_class(soup: btfl_sp) -> str:
    weight_class_rs = soup.find_all(name="h4", class_="single-fight__title text-center")
    # find_get_weight_class_start_index(weight_class)
    if is_weight_class_accessible(weight_class_rs):
        idx = find_get_weight_class_start_index(weight_class_rs)
        return weight_class_rs[idx].get_text().split('@')[-1].lstrip()
    else:
        return get_weight_class_alternative(soup)


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
    
    

    i = find_get_stats_start_index(stat_scrape)

    for key in stats.keys():
        if key == 'name':
            stats['name'] = get_name(soup)

        elif key == 'weightClass':
            
            stats['weightClass'] = get_weight_class(soup)

        elif i==len(stat_scrape):
            stats[key] = get_rank(soup, key)

        else:
            stats[key] = stat_scrape[i].get_text().replace(
                '\n', '').replace("\'", "'").strip()

            i += 1
    

    return stats
