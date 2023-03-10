import string
import requests
from tqdm import tqdm
import csv
from bs4 import BeautifulSoup, SoupStrainer
import re



html = requests.get('https://www.sliit.lk/computing/programmes/')
s = BeautifulSoup(html.content, 'html.parser')

results00 = s.find('div', class_='row gutter-xs')
degree = results00.find_all('a')


degreeLinkArray=[]
degreeCurtinLinkArray=[]

for link in degree[2:len(degree)-7]:
    if link.has_attr('href'):
        
        if (link.text).__contains__("– Curtin University"):
            degreeCurtinLinkArray.append(link['href'])
            print("curtin")
        else:
            degreeLinkArray.append(link['href'])
            print("normal")

with open('Sliit_Computing.csv', 'w', newline='') as file:

    for x in range(0, len(degreeLinkArray)):
        
        html = requests.get(degreeLinkArray[x])
        s = BeautifulSoup(html.content, 'html.parser')
        
        degreeName= s.find('h3', class_='tbk__title')
        degreeName2= s.find('h3', class_='tbk__subtitle')

        degreeNameText=degreeName.text +" "+ degreeName2.text

        degreeNameText = degreeNameText.replace('\r','')
        degreeNameText = degreeNameText.replace('\n','')

        details1 = s.find_all('span',class_='znListItems-text')

        size=len(details1)
        
        for y in range(0,size):
            if (details1[y].text).__contains__("Duration :"):
                duration=details1[y].text
            
            if (details1[y].text).__contains__("Location :"):
                location=details1[y].text
                
        Write=[degreeNameText,"Computing",location,"Degree",duration,"Full Time","Normal",degreeLinkArray[x]]

        writer = csv.writer(file)
        writer.writerows([Write])

    for x in range(0, len(degreeCurtinLinkArray)):
         
        html = requests.get(degreeCurtinLinkArray[x])
        s = BeautifulSoup(html.content, 'html.parser')        
                    
        r0 = s.find_all('div',class_='content-container')
        d1 = s.find_all('p')

        print(d1[0])
        print(d1[1])
        print(d1[3])
        print(d1[4])
        print(d1[5])

        W1=[d1[0].text,"Computing","Location :"+d1[5].text,"Degree","Duration :"+d1[4].text,d1[1].text,"Curtin University",degreeCurtinLinkArray[x]]
        writer = csv.writer(file)
        writer.writerows([W1])
                
    
