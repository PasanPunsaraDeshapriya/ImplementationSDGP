import string
import requests
from tqdm import tqdm
import csv
from bs4 import BeautifulSoup, SoupStrainer

html = requests.get('https://www.nibm.lk/faculties/school-of-business/')
s = BeautifulSoup(html.content, 'html.parser')

try:
    results00 = s.find('div', id='degree')
    degree = results00.find_all('a')
except:
    pass

try:
    results01 = s.find('div', id='higher-national-diploma')
    highernationaldiploma = results01.find_all('a')
except:
    pass

try:
    results02 = s.find('div', id='diploma-advanced-programmes')
    diplomaadvancedprogrammes = results02.find_all('a')
except:
    pass

try:
    results03 = s.find('div', id='diploma-programmes')
    diplomaprogrammes = results03.find_all('a')
except:
    pass

try:
    results04 = s.find('div', id='advanced-certificate-programmes')
    advancedcertificateprogrammes = results04.find_all('a')
except:
    pass

try:
    results05 = s.find('div', id='certificates-programmes')
    certificatesprogrammes = results05.find_all('a')
except:
    pass

try:
    results06 = s.find('div', id='foundation-programmes')
    foundationprogrammes = results06.find_all('a')
except:
    pass

try:
    results07 = s.find('div', id='professional-certification')
    professionalcertification = results07.find_all('a')
except:
    pass


degreeLinkArray = []
try:
    
    for link in degree:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in highernationaldiploma:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in diplomaadvancedprogrammes:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in diplomaprogrammes:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in advancedcertificateprogrammes:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in certificatesprogrammes:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in foundationprogrammes:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

    for link in professionalcertification:
        if link.has_attr('href'):
            degreeLinkArray.append(link['href'])

except:
    pass

print(degreeLinkArray)

print(len(degreeLinkArray))
with open('school-of-business.csv', 'w', newline='') as file:
    for x in range(0, len(degreeLinkArray)):
        html = requests.get(degreeLinkArray[x])
        s = BeautifulSoup(html.content, 'html.parser')

        try:

            results0 = s.find('div', class_='short-info-box fullwidth')
            duration = results0.find_all('span')

            results1 = s.find('div', class_='programme-title-name')
            degreeName = results1.find_all('h1')

            results2 = s.find('div', class_='programme-intro fullwidth')
            description = results2.find_all('p')

            print(x)
            print(degreeName[0].text)
            print(duration[0].text)
            print(duration[1].text)
            print(duration[3].text)
            print(degreeLinkArray[x])

            if duration[1].text == 'Business Analytics Centre':

                display = [degreeName[0].text, duration[0].text, duration[2].text, duration[3].text, duration[4].text,
                           degreeLinkArray[x]]
            else:
                display = [degreeName[0].text, duration[0].text, duration[1].text, duration[2].text, duration[3].text,
                           degreeLinkArray[x]]

            writer = csv.writer(file)
            writer.writerows([display])


        except:
            pass




