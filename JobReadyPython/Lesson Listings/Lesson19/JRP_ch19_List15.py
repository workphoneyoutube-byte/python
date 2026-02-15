import csv,os

count = 0
filename='data/transactions.csv'
dataset = {}

trans_date = input("Please the transaction date: ")
customer = input("Enter the customer: ")
merchant = input("Enter the merchant name: ")
total = input("Enter the total of the transaction: ")

input_data = {"trans_date":trans_date,"customer":customer,
"merchant":merchant,"total":total}
print(input_data)

fieldnames = ["trans_date","customer","merchant","total"]

# Open file in append mode, which will add the data at the 
# end of the  file
if os.path.exists(filename):
    with open(filename, 'a') as csv_file: 
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writerow(input_data)
else:
    with open(filename, 'w') as csv_file: 
      writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
      writer.writeheader()
      writer.writerow(input_data)

# Print out the data in the file:  
f = open('data/transactions.csv', 'r')
print(f.read())
f.close()
