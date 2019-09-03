import requests
from openpyxl import load_workbook

BASE_URL = r'https://vefa.difi.no/smp/'

wb = load_workbook('sap_sheet.xlsx', data_only=True)
sheet = wb.get_sheet_by_name('2) Input sheet')
tax = sheet['G3'].value
