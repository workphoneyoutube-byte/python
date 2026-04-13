from extract import extract #import our custom built extract module

class transform:

   #return the top N records from the dataset
   def head(self, dataset, step): 
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[0:step] 

   #return the last N records from the dataset
   def tail(self, dataset, step): 
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if step < 1:
           raise Exception("The step value must be positive.")
       return dataset[len(dataset) - step:len(dataset)]

   #rename a column in the dataset
   def rename_attribute(self, dataset, attribute, new_attribute): 
       if not dataset:
           raise Exception("Dataset cannot be empty.")
       if not attribute:
           raise Exception("The attribute key must be a valid key.")
       new_dataset = list()
       for row in dataset:
           if attribute in row.keys():
               val = row[attribute]
               new_row = row.copy()
               del new_row[attribute]
               new_row[new_attribute] = val
               new_dataset.append(new_row)
           else:
               raise Exception("Operation is not possible because the column " + \
                               str(column_name) \
                               + " does not exist in one of the rows in the dataset")
       return new_dataset

   #remove a column from the dataset
   def remove_attribute(self, dataset, attribute): 
       new_dataset = list()
       for row in dataset:
           new_row = row
           if attribute in new_row.keys():
               del new_row[attribute]
               new_dataset.append(new_row)
       return new_dataset

e = extract()
dataset = e.fromCSV(file_path = "data/stocks.csv")
print("Original dataset:")
print(dataset[0])

t = transform()
new_dataset = t.remove_attribute(dataset = dataset, attribute = "Open")
print("\nTransformed dataset:")
print(new_dataset[0])
