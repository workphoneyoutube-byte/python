tax_income = 150000

if tax_income <= 9875:
    tax_due = tax_income * 0.1
elif tax_income <= 40125:
    tax_due = (9875 * .1) + ((tax_income - 9875) * .12)
elif tax_income <= 85525:
    tax_due = (9875 * .1) + ((40125 - 9875) * .12) + ((tax_income - 40125) * .22)
elif tax_income <= 163300:
    tax_due = (9875 * .1) + ((40125 - 9875) * .12) + ((85525 - 40125) * .22) + ((tax_income - 85525) * .24)
    

# print the result
print(tax_due)
