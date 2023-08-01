# # Build a tip calculator.
print("Welcome to the tip calculator")
value_bill = float(input("what's the total bill? $"))
value_tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_pay = int(input("How many people to split the bill? "))

indivdual_bill = (value_bill / number_of_pay)
total = indivdual_bill + ((value_bill * (value_tip / 100)) /number_of_pay)

print("Each person should pay: $ %.2f" %(total))
