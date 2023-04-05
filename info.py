import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]

with open('hrefs.txt','r') as file:
    urls = file.read().splitlines()

for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        college=soup.find('div',class_='org-title col-span-8').find('h1',class_="title-font text-xl md:text-4xl pb-1 md:pb-4 font-bold leading-5 py-4 z-20").text.strip()
        #if college:
              #college_text=college.text.strip().replace('✓','')
        #else:
             # college_text=''
        #University = soup.find('ul',class_="flex flex-col bg-gray-100 pt-8 rounded-r-2xl text-sm text-gray-500").find('li', title='Accreditation').text
        data={
               'College':college.replace('✓','')
                #'University':University
        }
        datalist.append(data)
        
df=pd.DataFrame(datalist)
df.to_csv('college.csv',index=True)
