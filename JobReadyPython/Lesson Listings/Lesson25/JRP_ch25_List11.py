# new custom extract method
@staticmethod
def fromCustom(custom_extractor,**kwds):

    #this will execute the custom_extractor and store the data in dataset. 
    dataset = custom_extractor(**kwds)

    #if the type of dataset is not a list then we need to throw an error 
    if type(dataset)!= list:
        raise ValueError("Output data from extract step should a be list of items.")
    return dataset
