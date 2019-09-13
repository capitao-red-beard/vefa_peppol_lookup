import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup


BASE_URL = r"https://vefa.difi.no/smp"

dict_values = {'DE:VAT': '9930',
               'MK:VAT': '9942',
               'SI:VAT': '9949',
               'RO:VAT': '9947',
               'RS:VAT': '9948',
               'LU:VAT': '9938',
               'CY:VAT': '9928',
               'BA:VAT': '9924',
               'LV:VAT': '9939',
               'PT:VAT': '9946',
               'HR:VAT': '9934',
               'DK:CVR': '9902',
               'NO:ORG': '0192',
               'HU:VAT': '9910',
               'IE:VAT': '9935',
               'TR:VAT': '9952',
               'PL:VAT': '9945',
               'AT:VAT': '9914',
               'GB:VAT': '9932',
               'SK:VAT': '9950',
               'FR:VAT': '9957',
               'LT:VAT': '9937',
               'BE:VAT': '9925',
               'EE:VAT': '9931',
               'CZ:VAT': '9929',
               'SE:ORGNR': '0007',
               'MT:VAT': '9943',
               'NL:VAT': '9944',
               'CH:VAT': '9927',
               'BG:VAT': '9926',
               'ES:VAT': '9920',
               'NL:KVK': '0106',
               'FI:OVT': '0037',
               'IT:VAT': '9906'}

# Load the sheet and load in values rather than formulas.
wb = load_workbook("sap_sheet.xlsx", data_only=True)
sheet = wb["2) Input sheet"]
results_data = {}

for i in range(3, 4): #2264
    search_value = sheet["G" + str(i)].value
    input_scheme = sheet["F" + str(i)].value
    if 'VAT' in input_scheme:

        code = dict_values.get(input_scheme)

        url = f"{BASE_URL}/{code}/{search_value}"

        r = requests.get(url)
        if "not registered in SML." in r.text:
            results_data[search_value] = 'Not registered in SML'
        else:
            soup = BeautifulSoup(r.text, "html.parser")

            # 'dd' finds all the output values required for VAT.
            output = soup.findAll("dd")
            results_list = [str(i).replace("<dd>", "").replace("</dd>", "")
                            for i in output]
            results_data[search_value] = results_list


            # Find all of the document formats returned in the page.
            documents = soup.findAll("small", {"class": "meta"})

            soup_2 = BeautifulSoup(str(documents), "html.parser")
            data = soup_2.findAll("span")
            print(data)

with open('results.txt', 'w+') as f:
    f.write(str(results_data))

print('Done')
# TODO retrieve ONLY the values from the html.
