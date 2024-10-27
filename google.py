import requests
from bs4 import BeautifulSoup
import re

def get_asins_from_google(keywords):
    headers = {
        "User-Agent": "Your User-Agent Here"
    }
    search_query = f"{keywords} site:amazon.com"
    google_search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
    response = requests.get(google_search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        asin_pattern = re.compile(r'/dp/(\w{10})')
        asins = []

        for link in soup.find_all('a', href=True):
            match = asin_pattern.search(link['href'])
            if match:
                asins.append(match.group(1))
        print(asins)
        return list(set(asins))  # Removing duplicates
    else:
        print(f"Failed to retrieve Google results: Status code {response.status_code}")
        return []