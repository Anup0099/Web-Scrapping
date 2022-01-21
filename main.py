from asyncore import write
from cgitb import html
from gettext import find
from time import time
from turtle import pu
from bs4 import BeautifulSoup
import requests
import time

# with open('home.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     # print(soup.prettify())
#     # courses_html_tags = soup.find_all('h5')
#     # for course  in courses_html_tags:
#     #     print(course.text)


#     course_cards= soup.find_all('div', class_='card')
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]
#         # print(course_name)
#         # print(course_price)
#         print(f'{course_name} costs {course_price}')
print('Put some skill that you are not familiar with ')
unfamiliar_skill = input('>')
print(f'You are learning {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate( jobs):
        published_date = job.find(
            'span', class_='sim-posted').span.text.replace(' ', '')
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info =job.header.h2.a['href']
        
            if unfamiliar_skill not in skills:

                with open (f'posts/{index}.html','w') as f:
                # print(published_date)
                    # print(f'''company name: {company_name}
                    # skills: {skills}''')
                    f.write(f"Company name: {company_name.strip()}")
                    f.write(f"Skills: {skills.strip()}")
                    f.write(f'More info: {more_info} ')


                print('File saved: {index} ')

if __name__ == '__main__':
    while True:
       find_jobs()
       time_wait =10
       print(f'Waiting {time_wait} minutes...')
       time.sleep(time_wait*60) 