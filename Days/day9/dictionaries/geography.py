capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# - Nesting a Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  "total_visits": 5},
}


# -  Nesting a Dictionary in a list

travel_log = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  "total_visits": 5},
]

def add_new_country(country_visited, times_visited, cities_visited)

def add_new_country(log, country, total_visits, cities):
    new_travel_entry = {}
    new_travel_entry["country"] = country
    new_travel_entry["cities"] = cities
    new_travel_entry["total_visits"] = total_visits

    log.append(new_travel_entry)

    return log
    