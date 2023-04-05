import string
import requests
from tqdm import tqdm
import csv
from bs4 import BeautifulSoup, SoupStrainer
import re

html = requests.get('https://www.nsbm.ac.lk/faculty/faculty-of-science/')
s = BeautifulSoup(html.content, 'html.parser')

results00 = s.find('div',class_='col-lg-12')
degree = results00.find_all('a')

degreeLink=[]
foundationLink=[]


for link in degree[0:len(degree)]:

    if link.has_attr('href'):
        
        if (link.get('href')).__contains__("foundation"):
            print('f')
            foundationLink.append(link.get('href'))
        else:
            print('d')
            degreeLink.append(link.get('href'))


print(foundationLink)
print(" ")
print(degreeLink)

with open('NSBM_Science.csv', 'w', newline='') as file:



#Degree
    for x in range(0, len(degreeLink)):

        html = requests.get(degreeLink[x])
        s = BeautifulSoup(html.content, 'html.parser')
        
#degree name
        
        degreeName= s.find_all('h1', class_='header-course')
        print(" ")
        print("Name: "+degreeName[0].text)
        degreeNameAff=""
        found=0
        
        print("hello")
  
        if (degreeName[0].text).__contains__("Plymouth"):
            print("             ")
            print("PLYMOUTH UNIVERSITY")
            print("             ")
            degreeNameAff="PLYMOUTH UNIVERSITY"
        elif (degreeName[0].text).__contains__("Victoria"):
            print("             ")
            print("VICTORIA UNIVERSITY")
            print("             ")
            degreeNameAff="VICTORIA UNIVERSITY"
        else:
            print("             ")
            print("NSBM")
            print("             ")
            degreeNameAff="NSBM"

        
#details

        details = s.find_all('div',class_='course-year')
        
        details1=(details[0].text).split()
        print(details1[0]+" "+details1[1])

        details2 = s.find('div',class_='course-year-2')
        Year=(details2.text).strip('\n')
        

#Writing


        Write=[degreeName[0].text,"Science","Pitipana - Thalagala Rd, Homagama","Degree",Year,details1[0]+" "+details1[1],degreeNameAff,degreeLink[x]]
        print(Write)        

        writer = csv.writer(file)
        writer.writerows([Write])

#Foundation
    for x in range(0, len(foundationLink)):

        html = requests.get(foundationLink[x])
        s = BeautifulSoup(html.content, 'html.parser')
        
#degree name
        
        degreeName= s.find_all('h1', class_='header-course')
        print(" ")
        print("Name: "+degreeName[0].text)
        degreeNameAff=""
        found=0
        
        print("hello")
  
        if (degreeName[0].text).__contains__("Plymouth"):
            print("             ")
            print("PLYMOUTH UNIVERSITY")
            print("             ")
            degreeNameAff="PLYMOUTH UNIVERSITY"
        elif (degreeName[0].text).__contains__("Victoria"):
            print("             ")
            print("VICTORIA UNIVERSITY")
            print("             ")
            degreeNameAff="VICTORIA UNIVERSITY"
        else:
            print("             ")
            print("NSBM")
            print("             ")
            degreeNameAff="NSBM"

        
#details

        details = s.find_all('div',class_='course-year')
        
        details1=(details[0].text).split()
        print(details1[0]+" "+details1[1])

        details2 = s.find('div',class_='course-year-2')
        Year=(details2.text).strip('\n')
        

#Writing


        Write=[degreeName[0].text,"Science","Pitipana - Thalagala Rd, Homagama","Foundation",Year,details1[0]+" "+details1[1],degreeNameAff,foundationLink[x]]
        print(Write)        

        writer = csv.writer(file)
        writer.writerows([Write])
        
        
