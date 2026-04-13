import json

from pprint import pprint 

with open('data/prize.json','r') as jsonfile: 
    data = json.load(jsonfile) # load the json content and serialize it. 
print(type(data)) #dict
pprint(data)      # print the entire file content. 
