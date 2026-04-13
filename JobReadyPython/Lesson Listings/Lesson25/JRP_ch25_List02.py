from extract import extract

dataset = extract.fromCSV(file_path = "data/stocks.csv")
print(dataset[0])
