def read_csv(filepath,delimiter=","):
    import csv
    dataset = list()
    with open(filepath) as f: 
        csv_file = csv.DictReader(f, delimiter=delimiter) 
        for row in csv_file:
            dataset.append(row)
    return dataset

dataset = read_csv("data/stocks.csv")
total = 0
for row in dataset:
  total += float(row["Close"])
  print("Close: " + str(row["Close"]))
  print("----")print(total)
