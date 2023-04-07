import requests
from bs4 import BeautifulSoup
import pandas as pd

urls=['https://www.collegenp.com/colleges']
with open('hrefs.txt', 'w') as file:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        parent_links = soup.find('div',class_="media-body")
        if parent_links:
            for link in parent_links:
                href_value = link.find('a').get('href')
                file.write(href_value + '\n')
        else:
            print("None")


