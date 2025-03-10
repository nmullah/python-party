import pip
import requests
from bs4 import BeautifulSoup

def google_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results = [g.get_text() for g in soup.find_all('h3')]
        return results
    else:
     return [f"Failed to fetch results, status code: {response.status_code}"]

if __name__ == "__main__":
    query = input("Enter search query: ")
    results = google_search(query)
    
    print("\nTop search results:")
    for idx, result in enumerate(results, 1):
        print(f"{idx}. {result}")