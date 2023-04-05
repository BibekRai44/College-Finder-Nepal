import requests
from bs4 import BeautifulSoup

urls = ['https://edusanjal.com/college/?page=1']

with open('hrefs.txt', 'w') as file:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        parent_links = soup.find_all('div', class_="overflow-hidden bg-white rounded shadow-xl")
        if parent_links:
            for link in parent_links:
                href_value = link.find('a').get('href')
                file.write("https://edusanjal.com"+href_value + '\n')
        else:
            print("None")
