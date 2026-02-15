def head(filepath,num_char):
  f = open(filepath, mode="r")
  output = f.read(num_char)
  f.close()
  return output

# return the first 20 characters in the file data/text.txt
text = head("IncidentTicket.txt",20) 
print(text)
