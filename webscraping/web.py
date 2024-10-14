import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue')
# success code 
print(r)

# print content of requests 
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())


table = soup.find('table', {'class': 'wikitable sortable'})

headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())  #Strip whitespaces


# Extract the table rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skip the header row
    cells = tr.find_all(['td', 'th'])
    row = [cell.text.strip() for cell in cells]
    rows.append(row)


# Create a DataFrame using Pandas for easy data handling

df = pd.DataFrame(rows, columns=headers)

print(df)


# Save the data to a CSV file

df.to_csv('largest_us_companies.csv', index=False)

print("Data has been saved to 'largest_us_companies.csv' .")