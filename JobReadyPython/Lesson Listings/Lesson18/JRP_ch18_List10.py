def line_starts_with(file_path,fchar):
  f = open(file_path, mode="r")
  output = ""
  for line in f:
    if fchar == line[0]:
      output += line
  return output

# return all lines in the file data/text.txt that start with "I". 
text = line_starts_with("IncidentTicket.txt","I")
print(text)
