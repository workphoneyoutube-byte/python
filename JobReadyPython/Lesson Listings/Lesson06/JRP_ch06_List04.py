# define user input
gross_inc = input("Enter your gross income from your W-2 for 2020: ")
# print(gross_inc)

num_dep = input("How many dependents are you claiming? ")
# print(num_dep)

#calculate taxable income
tax_income = gross_inc - 12200 - (2000 * num_dep)
print (tax_income)
