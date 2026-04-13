# Update the following code according to the instructions above.

class extract:
  def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
    if not file_path:
      raise Exception("You must provide a valid file path.")
    import csv
    dataset = list()
    with open(file_path) as f: 
      csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar) 
      for row in csv_file:
        dataset.append(row)
    return dataset
 
  def fromJSON(self, file_path):
    if not file_path:
      raise Exception("You must provide a valid file path.")
    import json
    dataset = list()
    with open(file_path) as json_file:  
      dataset = json.load(json_file)
    return dataset
  
e = extract()
dataset1 = e.fromCSV(file_path="data/missing_file.csv")
dataset2 = e.fromJSON(file_path="data/missing_file.json")
