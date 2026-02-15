import json

with open('data/prize.json','r') as jsonfile: 
    # use the json module with the load function 
    # to read the entire content of the json file
    data = json.load(jsonfile) 

# iterate through the file and display each json object separately. 
for k in data['prizes']: 
    print(k)
