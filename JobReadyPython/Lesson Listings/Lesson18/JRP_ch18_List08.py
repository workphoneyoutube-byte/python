def head(filepath,num_lines):
    f = open(filepath, mode="r")
    lines = ""
    for x in range(num_lines):
      lines += f.readline()
    f.close()
    return lines 

# return the first 3 lines in the file 
text = head("IncidentTicket.txt",3) 
print(text)
