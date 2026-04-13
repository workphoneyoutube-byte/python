class CheckingAccount:
    type = "checking"
    def __init__(self,id,balance):
        self.account_id = id
        self.balance = balance
        
ch1 = CheckingAccount("ID3454", 123452)
ch2 = CheckingAccount("ID34632",959309)

print(ch1.type)
print(ch2.type)
