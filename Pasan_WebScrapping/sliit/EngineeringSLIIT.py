import string
import requests
from tqdm import tqdm
import csv
from bs4 import BeautifulSoup, SoupStrainer
import re



html = requests.get('https://www.sliit.lk/engineering/programmes/')
s = BeautifulSoup(html.content, 'html.parser')




results00 = s.find('div',class_='zn_section_size container zn-section-height--auto zn-section-content_algn--top')
print(results00)

degree = results00.find_all('a')

degreeEngLinkArray=[]

for link in degree[0:len(degree)]:
    
    print(link.text)
    
    if link.has_attr('href'):
        print('---------------')

        
        if (link.text).__contains__("Department"):
            print("Department")
        
        elif (link.text).__contains__("Engineering"):
            degreeEngLinkArray.append(link['href'])
            print("Engineering")

print(degreeEngLinkArray)

with open('Sliit_Engineering.csv', 'w', newline='') as file:
    
  for x in range(0, len(degreeEngLinkArray)):

        html = requests.get(degreeEngLinkArray[x])
        s = BeautifulSoup(html.content, 'html.parser')
#degree name
        try:
            degreeName= s.find('h3', class_='tbk__title')
            degreeName2= s.find('h3', class_='tbk__subtitle')
            
            degreeNameText=degreeName.text +" "+ degreeName2.text

            degreeNameText = degreeNameText.replace('\r','')
            degreeNameText = degreeNameText.replace('\n','')
            
        except:
            
           degreeName= s.find('h3', class_='tbk__title')
           degreeNameText=degreeName.text
           degreeNameText = degreeNameText.replace('\r','')
           degreeNameText = degreeNameText.replace('\n','')
           
        print(" ")
        print(degreeNameText)
        print(" ")

        
#details        
        details1 = s.find_all('span',class_='znListItems-text')

        
        duration=[' ']
        location=[' ']
        
        size=len(details1)
        
        for y in range(0,size):

            
            if (details1[y].text).__contains__("Duration :"):
                duration[0]=(details1[y].text)
                
                
            if (degreeEngLinkArray[x]).__contains__("Location :"):
                location[0]=(details1[y].text)
                

        if (degreeEngLinkArray[x]).__contains__("queensland"):

            if location[0]!=' ':

                Write=[degreeNameText,"Engineering",location[0],"Degree",duration[0],"Full Time","The University of Queensland",degreeEngLinkArray[x]]
                print(Write)
             
            else:
                Write=[degreeNameText,"Engineering","Location: Malabe","Degree","Duration: 4 Years","Full Time","The University of Queensland",degreeEngLinkArray[x]]
                print(Write)

        else:
            
            if location[0]!=' ':

                Write=[degreeNameText,"Engineering",location[0],"Degree",duration[0],"Full Time","Normal",degreeEngLinkArray[x]]
                print(Write)
             
            else:
                Write=[degreeNameText,"Engineering","Location: Malabe","Degree","Duration: 4 Years","Full Time","Normal",degreeEngLinkArray[x]]
                print(Write)


        writer = csv.writer(file)
        writer.writerows([Write]) 




            
