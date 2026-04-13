import csv

with open('data/stocks_short.csv') as f: 
    csv_file = csv.reader(f, delimiter=',')

    for row in csv_file:
        print(row[0], " - ", row[1] )
