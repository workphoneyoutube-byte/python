employees = ["Billy", "Jayden", "Magda", "Luis"]
for ctr in employees:    # iterate through the list of employees
  print(ctr)
  for ctr2 in ctr:       # iterate through each employee
     print(ctr2.upper())
  print("----")
