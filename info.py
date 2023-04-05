import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]

with open('hrefs.txt','r') as file:
    urls = file.read().splitlines()

for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        University = soup.find('span', class_="inline-flex justify-center h-12 w-12 text-lg").text
        data={
              'University':University
        }
        datalist.append(data)

df=pd.DataFrame(datalist)
df.to_csv('college.csv',index=True)
