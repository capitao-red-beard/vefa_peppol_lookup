import requests
from openpyxl import load_workbook

BASE_URL = r'https://vefa.difi.no/smp'

wb = load_workbook('sap_sheet.xlsx', data_only=True)
sheet = wb['2) Input sheet']
tax = sheet['G3'].value
identifier = '9944'

url = f'{BASE_URL}/{identifier}/{tax}'
print(url)

r = requests.get(url)
print(r.status_code)
