import requests
from bs4 import BeautifulSoup
import csv

# Send a request to the website
url = 'https://www.ugc.ac.lk/index.php?option=com_content&view=article&id=101&Itemid=37&lang=en'
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the data
table = soup.find('div', class_='article-content')

# Find all the rows in the table
rows = table.find_all('tr')

# Open a CSV file for writing
with open('ugc_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Loop through each row and extract the data
    for row in rows:
        # Extract the cells in the row
        cells = row.find_all('td')

        # Convert the cell data to text and write it to the CSV file
        writer.writerow([cell.get_text(strip=True) for cell in cells])
