acctBal = 13445;
locBal = 16000;
savBal = 4000;
savInterest = .025;
locInterest = .098;
months = 12;
years = 8.5;
numString = "12345"

compInt = savBal * ((1 + (savInterest/months))**(months*years))
print(round(compInt,2))
result1 = (savBal+acctBal)-locBal
print(result1)
result2 = (acctBal-locBal)*locInterest
print(round(result2,2));
result3 = ((savInterest/months)+1)**(months*years)
print(result3);
result4 = ((locInterest*months*years)+1)*locBal
print(round(result4,1))
