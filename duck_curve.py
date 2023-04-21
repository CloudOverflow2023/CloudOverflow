import csv
with open('mock_data.csv', 'r') as csvfile:
    csvreader = csv.reader(file)
    for row in csvreader:
        print (row)
    