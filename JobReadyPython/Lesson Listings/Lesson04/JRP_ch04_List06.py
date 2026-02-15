acctBal = 13445;
locBal = 16000;
savBal = 4000;
savInterest = .025;
locInterest = .098;

months = 12;
years = 8.5;
numString = "12345"

result1 = acctBal+savBal-locBal;
print(result1);
result2 = acctBal-locBal*locInterest;
print(result2);
result3 = savBal*months*savInterest;
print(result3);
result4 = acctBal/savBal/locBal;
print(result4);
result5 = savBal*1+savInterest/months**years;
print(result5)
