import json
import csv 

with open('prof.json', 'r') as json_file:
    data = json.load(json_file)

data_file = open('prof.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
header = data[0].keys()
csv_writer.writerow(header)
for row in data:
    csv_writer.writerow(row.values())
data_file.close