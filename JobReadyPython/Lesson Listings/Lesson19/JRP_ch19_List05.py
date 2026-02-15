import csv

with open('data/stocks_short.csv') as f: 

    csv_file = csv.DictReader(f, delimiter=',') 

    # csv_file is an iterable object that we can iterate on using a for loop
    for row in csv_file:
        print(row) 
