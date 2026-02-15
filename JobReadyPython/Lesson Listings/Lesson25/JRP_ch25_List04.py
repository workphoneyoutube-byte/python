from extract import extract
from transform import transform

def round_open_price(value,*args):
    return round(float(value))


dataset = extract.fromCSV(file_path = "data/stocks.csv")
print(dataset[0])

new_dataset = transform.transform(dataset = dataset, attribute = "Open", 
                                  new_attribute = "open_price_rounded",
                                  transform_function = round_open_price)
print(new_dataset[0])
