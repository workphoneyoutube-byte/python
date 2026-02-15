acctBal = 13445;
locBal = 16000;
savBal = 4000;
savInterest = .025;
locInterest = .098;
months = 12;
years = 8.5;
numString = "12345"

compInt = savBal*((1 + (savInterest/months))**(months*years))
print(compInt)
result1 = (savBal+acctBal)-locBal
print(result1)
result2 = (acctBal-locBal)*locInterest
print(result2);
result3 = ((savInterest/months)+1)**(months*years)
print(result3);
