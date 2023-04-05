import string
import requests
from tqdm import tqdm
import csv
from bs4 import BeautifulSoup, SoupStrainer
import re

html = requests.get('https://www.iit.ac.lk/computing/')
s = BeautifulSoup(html.content, 'html.parser')

results00 = s.find('div',class_='middle-wrap simple-padding-top simple-padding-bottom')
degree = results00.find_all('p')

degreeLink=[]
foundationLink=[]
masterLink=[]

for link in degree[0:len(degree)]:

    if link.has_attr('href'):
        print("hello")
        if (link.get('href')).__contains__("foundation"):
            print('f')
            foundationLink.append(link.get('href'))
        elif (link.get('href')).__contains__("bsc") or (link.get('href')).__contains__("beng"):
            print('d')
            degreeLink.append(link.get('href'))
        elif (link.get('href')).__contains__("msc"):
            print('m')
            masterLink.append(link.get('href'))

print(foundationLink)
print(" ")
print(degreeLink)
print(" ")
print(masterLink)

with open('IIT_Computing.csv', 'w', newline='') as file:

#FOUN        
    for x in range(0, len(foundationLink)):

        html = requests.get(foundationLink[x])
        s = BeautifulSoup(html.content, 'html.parser')
#degree name
        
        degreeName= s.find('h1', class_='section-heading section-heading--white js-scroll scrolled fade-in-bottom') 
        
        print(degreeName.text)

#details


        duration = s.find_all('div',class_='intake-box-inner position-relative')
                
        duration1=(duration[1].text).split()
        print(duration1)

        if(len(duration1)==3):
        
            Write=[degreeName.text,"Computing","57 Ramakrishna Rd, Colombo 00600","Foundation",duration1[1]+" "+duration1[2],"Full Time","Informatics Institute of Technology",foundationLink[x]]

        else:

            Write=[degreeName.text,"Computing","57 Ramakrishna Rd, Colombo 00600","Foundation",duration1[1]+" "+duration1[2],duration1[3]+" "+duration1[4],"Informatics Institute of Technology",foundationLink[x]]


        print(Write)
        writer = csv.writer(file)
        writer.writerows([Write])

#DEGREE
    for x in range(0, len(degreeLink)):

        html = requests.get(degreeLink[x])
        s = BeautifulSoup(html.content, 'html.parser')
#degree name
        
        degreeName= s.find('h1', class_='section-heading section-heading--white js-scroll scrolled fade-in-bottom') 
        
        print(degreeName.text)

#details


        duration = s.find_all('div',class_='intake-box-inner position-relative')
                
        duration1=(duration[1].text).split()
        print(duration1)

        if(len(duration1)==3):
        
            Write=[degreeName.text,"Computing","57 Ramakrishna Rd, Colombo 00600","Degree",duration1[1]+" "+duration1[2],"Full Time","University of Westminster",degreeLink[x]]

        else:

            Write=[degreeName.text,"Computing","57 Ramakrishna Rd, Colombo 00600","Degree",duration1[1]+" "+duration1[2],duration1[3]+" "+duration1[4],"University of Westminster",degreeLink[x]]


        print(Write)
        writer = csv.writer(file)
        writer.writerows([Write])

#MAST
    for x in range(0, len(masterLink)):

        html = requests.get(masterLink[x])
        s = BeautifulSoup(html.content, 'html.parser')
#degree name
        
        degreeName= s.find('h1', class_='section-heading section-heading--white js-scroll scrolled fade-in-bottom') 
        
        print(degreeName.text)

#details


        duration = s.find_all('div',class_='intake-box-inner position-relative')
                
        duration1=(duration[1].text).split()
        print(duration1)

        if(len(duration1)==3):
        
            Write=[degreeName.text,"Computing","57 Ramakrishna Rd, Colombo 00600","Master",duration1[1]+" "+duration1[2],"Full Time","University of Westminster",masterLink[x]]

        else:

            Write=[degreeName.text,"Computing","57 Ramakrishna Rd, Colombo 00600","Master",duration1[1]+" "+duration1[2],duration1[3]+" "+duration1[4],"University of Westminster",masterLink[x]]


        print(Write)
        writer = csv.writer(file)
        writer.writerows([Write])

        
    






















            
