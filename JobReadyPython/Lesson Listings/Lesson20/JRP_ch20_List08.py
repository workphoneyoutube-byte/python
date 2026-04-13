import json

filename = 'data/bank_transactions.json'

with open(filename,'r') as jsonfile:
  data = json.load(jsonfile)

total = 0
total_balance = 0

for each in data:
  if each['WITHDRAWAL AMT'] != '':
    total +=  float(each['WITHDRAWAL AMT'])
  if each['BALANCE AMT'] != '':
    total_balance +=  float(each['BALANCE AMT'])

print("Total Withdrawals: ", total)
print("Total of Balances: ", total_balance)
