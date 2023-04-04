import requests
from bs4 import BeautifulSoup
urls=['https://www.linkedin.com/jobs/search/?currentJobId=3531688286&distance=25&geoId=104630404&keywords=jobs&location=Nepal&refresh=true']

with open('hrefs.txt', 'w') as file:

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        parent_links = soup.find('a', class_="disabled ember-view job-card-container__link job-card-list__title")
        if parent_links:
            href_value=parent_links.get('href')
            file.write(href_value + '\n')
        else:
            print("None")
