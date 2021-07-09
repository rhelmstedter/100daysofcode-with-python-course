import requests
from collections import namedtuple
from typing import List

Search_result = namedtuple("Search_result", "number, category, id, url, title, description")

def search_site(keywords: str) -> List[Search_result]:
    url = f"https://search.talkpython.fm/api/search?q={keywords}"
    resp = requests.get(url)
    resp.raise_for_status()
    results = resp.json()

    search_results = []
    result_number = 1
    for r in results.get("results"):
        if r["category"] == "Episode":
            search_results.append(Search_result(number=result_number, **r))
            result_number += 1

    return search_results
