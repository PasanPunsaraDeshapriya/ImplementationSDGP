import string
import requests
from bs4 import BeautifulSoup

url = 'https://www.ugc.ac.lk/index.php?option=com_university&view=list&Itemid=25&lang=en'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find('div', id='ugc-current-content')
job_title = results.find_all('span', class_='Tips2')

f = open("dataset_university_SL.csv", "w")
for job in job_title:
    f.write(job.text.translate(str.maketrans('','',string.punctuation)))

f.close()
