import xlrd
from collections import OrderedDict
import simplejson as json

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('excel/dataset_nuovo.xlsx')
sh = wb.sheet_by_index(5)

# List to hold dictionaries
dataset = []


# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = OrderedDict()
    row_values = sh.row_values(rownum)
    cars['descrizione'] = row_values[1]
    cars['results'] = row_values[3]


    dataset.append(cars)

# Serialize the list of dicts to JSON
j = json.dumps(dataset)

# Write to file
with open('JSON/300dim/RA30249_Training24201.json', 'w') as f:
    f.write(j)
