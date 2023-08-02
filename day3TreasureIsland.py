height = int(input("Enter your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y":
        bill += 3
    else:
        bill = bill
    print(f"Your final bill is ${bill}.")
    
else:
    print("Sorry, you have to grow taller before you can ride.")


# year = int(input("input year: "))

# if year % 4 == 0 & year % 100 == 0 & year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
    
# if add_pepperoni == "Y":
#     bill += 2
# elif size == "M" or "L":
#     bill += 3
# else:
#     bill = bill

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")
