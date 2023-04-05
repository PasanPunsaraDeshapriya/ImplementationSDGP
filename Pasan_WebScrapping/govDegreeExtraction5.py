import string
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def createURL(numberUni, numberFac):
    return 'https://www.ugc.ac.lk/index.php?option=com_university&id=' + str(
        numberUni) + '&view=unifaculty&facid=' + str(numberFac) + '&Itemid=25&lang=en'


for i in range(1, 41):
    for x in range(1, 117):

        html = requests.get(createURL(i, x))
        s = BeautifulSoup(html.content, 'html.parser')

        try:
            results1 = s.find('div', id='ugc-current-content')
            uni = results1.find_all('h2')
            print(uni)

            faculty = results1.find_all('strong')
            printFaculty = (faculty[0]).text
            printUni = (uni[0]).text

            results2 = s.find('div', id='ugc-current-content')
            job_title = results2.find_all('li')
            print(job_title)
            
            if len(job_title)!=0:
                f = open("dataset_university_" + printUni + "_" + printFaculty + ".csv", "w")
                for job in job_title:
                    f.write(job.text)
                    f.write("\n")
                f.close()
        except:
            pass
