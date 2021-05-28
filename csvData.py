import csv
from os import remove
filename = "Calllog.csv"
rows = []
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
finalListofNumbers = []
for row in rows:
    if(row['Type'] == 'Missed'):
        finalListofNumbers.append(row['Phone'])
    elif (row['Phone'] in finalListofNumbers):
        finalListofNumbers.remove(row['Phone'])

print(finalListofNumbers)
