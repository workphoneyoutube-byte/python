# 0001
## functions
def compute_max_value(**kwargs):
    if not kwargs:
        return None
    max_key = max(kwargs, key=kwargs.get)
    max_val = kwargs[max_key]
    print(f"Max: {max_key} = {max_val}")
    return max_key, max_val


compute_max_value(word_1=1, word_2=3, word_3=6, word_4=5)

#print(word,freq)

# 0002
## functions
#def compute_max_value(**kwargs):
#    for keyword,value in kwargs.items():
#        print(keyword + ": " + str(int(value)))
#    return None
#        
#compute_max_value(word_1 = 1, word_2 = 3, word_3 = 6, word_4 = 5)
#