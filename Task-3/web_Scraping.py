import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Send a GET request to the website
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract Quotes, Authors, and Tags
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

# Step 4: Open a CSV file to write the data
with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Step 5: Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Step 6: Write the header row
    writer.writerow(['Quote', 'Author', 'Tags'])
    
    # Step 7: Write the extracted data into the CSV file
    for i in range(len(quotes)):
        quote_text = quotes[i].text
        author = authors[i].text
        tag_list = [tag.text for tag in tags[i].find_all('a', class_='tag')]
        tags_string = ', '.join(tag_list)
        
        writer.writerow([quote_text, author, tags_string])

print("Data has been written to quotes.csv")
