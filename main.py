import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup


BASE_URL = r'https://vefa.difi.no/smp'

# Load the sheet and load in values rather than formulas.
wb = load_workbook('sap_sheet.xlsx', data_only=True)
sheet = wb['2) Input sheet']
tax = sheet['G3'].value

# TODO retrieve the identifier from the excel sheet.
identifier = '9944'

url = f'{BASE_URL}/{identifier}/{tax}'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# 'dd' finds all the output values required for VAT.
output = soup.findAll('dd')
results_list = [str(i).replace('<dd>', '').replace('</dd>', '')
                for i in output]
print(results_list)

# Find all of the document formats returned in the page.
documents = soup.findAll('small', {'class': 'meta'})

# TODO retrieve ONLY the values from the html.
