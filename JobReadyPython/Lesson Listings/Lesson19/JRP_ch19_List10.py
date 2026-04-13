import csv
with open('user_input.csv', 'w', newline='') as csv_file:
    
  while True:
    user_input = input("Please enter text to add to file [enter quit to exit]: ")
    if user_input.lower() == 'quit':
      break
    else:
      writer = csv.writer(csv_file,delimiter=',')
      writer.writerow([user_input])

f = open('user_input.csv', 'r')
print(f.read())
f.close()
