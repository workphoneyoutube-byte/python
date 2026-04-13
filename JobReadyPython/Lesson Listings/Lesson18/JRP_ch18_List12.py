import datetime

f = open("ReportFile.txt", "a") 

f.write("Acme Bank EBP")
f.write("\nDate:" + str(datetime.date.today()))
f.write("\nReport File 0001")

f.close() 
