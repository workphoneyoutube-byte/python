from lib import *

dataset = read_json_file("/Users/haythembalti/Downloads/reviews.json") 
print(dataset[0]) 

dataset_tokenized = tokenize_dataset(dataset)
print("Words of the first review:")
print(dataset_tokenized[0]['words'])
print("Words of the second review:")
print(dataset_tokenized[1]['words'])
print(type(dataset_tokenized))
