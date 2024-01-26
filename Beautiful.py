import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')

        for quote in quotes:
            print(quote.text)
    else:
        print(f"Failed to fetch quotes. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_quotes()
