import json

filename = 'data/bank_transactions.json'

with open(filename,'r') as jsonfile:
  data = json.load(jsonfile)

for each in data:
  if each['WITHDRAWAL AMT'] != '':
    val = float(each['WITHDRAWAL AMT'])
    if val > 650000:
      print(each['Account No'], "===>", val)

