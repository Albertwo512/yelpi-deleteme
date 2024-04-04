import requests
from typing import List
from config import APP_CONFIG
from pprint import pprint as pp

BASE_URL = f"https://api.yelp.com/v3/businesses/search"
    

HEADERS = {
        "accept": "application/json",
        "Authorization": f"Bearer {APP_CONFIG['API_KEY']}"
    }

def get_search_results(food: str, location: str) -> List:
    query = f"?location={location}&term={food}&sort_by=best_match&limit=20"
    url = BASE_URL + query
    response = requests.get(url, headers=HEADERS)
    businesses = response.json()['businesses']
    return businesses

if __name__ == '__main__':
    businesses = get_search_results(food='tacos', location= 'Guadalajara%20Jalisco')
    pp(businesses, compact=True)
