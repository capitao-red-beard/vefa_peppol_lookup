import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup


BASE_URL = r'https://vefa.difi.no/smp'

wb = load_workbook('sap_sheet.xlsx', data_only=True)
sheet = wb['2) Input sheet']
tax = sheet['G3'].value
identifier = '9944'

url = f'{BASE_URL}/{identifier}/{tax}'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
output = soup.findAll('dd')
documents = soup.findAll('small', {'class': 'meta'})
results_list = [str(i).replace('<dd>', '').replace('</dd>', '')
                for i in output]

print(results_list)
