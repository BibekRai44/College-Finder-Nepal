import requests
from bs4 import BeautifulSoup
import pandas as pd
datalist=[]

with open('hrefs.txt','r') as file:
    urls = file.read().splitlines()

for url in urls:
        response = requests.get(url)
       
        soup = BeautifulSoup(response.content, 'html.parser')
    
        college=soup.find('div',class_='org-title col-span-8')
        if college == None:
              continue
        h1 = college.find('h1',class_="title-font text-xl md:text-4xl pb-1 md:pb-4 font-bold leading-5 py-4 z-20").text.strip()
        if h1 == None:
              continue
       
        University = soup.find('ul',class_="flex flex-col bg-gray-100 pt-8 rounded-r-2xl text-sm text-gray-500").find('li', title='Accreditation').text.strip()
        owenership_type=soup.find('ul',class_="flex flex-col bg-gray-100 pt-8 rounded-r-2xl text-sm text-gray-500").find('li',title="Ownership").text.strip()

        phone_contact = ""
        email_contact = ""
    
        phone = soup.find('ul', class_="flex flex-col bg-gray-100 pt-8 rounded-r-2xl text-sm text-gray-500").find('li', title="Phone")
        if phone:
            phone_contact = phone.text.strip()
    
        email = soup.find('ul', class_="flex flex-col bg-gray-100 pt-8 rounded-r-2xl text-sm text-gray-500").find('li', title="Email")
        if email:
            email_contact = email.text.strip()
        
        location=soup.find('div',class_="text-base md:text-xl text-gray-600 leading-5 mb-2").text.strip()
        course_offered=soup.find_all('div',class_="flex justify-between mb-1")
        course_list = []
        for course in course_offered:
            course_list.append(course.find('a').text.strip())
            data={
               'College':h1.split('\n')[0],
               'Location':location,
               'University':University,
               'Course Offered':', '.join(course_list),
               'Ownership Type':owenership_type,
               'Phone Number':phone_contact,
               'Email':email_contact
                
        }

        datalist.append(data)
        
df=pd.DataFrame(datalist)
df.to_csv('college6.csv',index=True)
