import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com"
response = requests.get(url)

#check if request was succesful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

else:
    print("Failed to retreive the page")


quotes_data = []

#find all quote blocks
quotes = soup.find_all('div',class_='quote')

for quote in quotes:
    text = quote.find('span', class_ ='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_= 'tag')]

    quotes_data.append(
        {
            'text': text,
            'author': author,
            'tags' : tags
        }
    )

json_output = json.dumps(quotes_data, indent=4, ensure_ascii=False)
print(json_output)

with open('quotes.json', 'w') as f:
    json.dump(quotes_data, f, indent=4, ensure_ascii=False)