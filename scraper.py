import requests
from bs4 import BeautifulSoup
urls=['https://www.linkedin.com/jobs/search/?currentJobId=3531688286&distance=25&geoId=104630404&keywords=jobs&location=Nepal&refresh=true']

with open('hrefs.txt', 'w') as file:

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        parent_links = soup.find_all('div', class_='full-width artdeco-entity-lockup__title ember-view')
        for parent_link in parent_links:
            children = parent_link.find('a',class_="disabled ember-view job-card-container__link job-card-list__title")
            href_value = "https://www.linkedin.com/" + children.get('href')
            file.write(href_value + '\n')
