import os,csv

while True:
  if os.path.exists('data/user_input.csv'):
    user_prompt= input("The file exists, what data would you like to append? [type quit to exit]: ")
    if user_prompt.lower() == 'quit':
      break
    else:
      with open('data/user_input.csv', 'a') as csv_file: 
        writer = csv.writer(csv_file,delimiter=',')  
        writer.writerow([user_prompt]) # writing the first row
  else:
    f = open('data/user_input.csv','w')
    print("The file data/user_input.csv does not exist. It has been created.")

f = open('data/user_input.csv','r')
print(f.read())
f.close()
