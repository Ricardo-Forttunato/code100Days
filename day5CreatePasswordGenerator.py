# for loop with lists.
# fruits = [ "Apple","Peach", "Pear"]
# for fruit in fruits:
#     # print(fruit)
#     # print(fruit + " Pie") # This is inside the for loop.
# # print(fruits) # This is outside the for loop.

# Average height calculator.
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])  
# average_height = round((sum(student_heights)/len(student_heights)))
# # print(average_height)

# student_scores = input("Input a list of student scores ").split()

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# for score in student_scores:
#     if score > student_scores[0]:
#         student_scores[0] = score
#     else:
#         score = student_scores[0]
# print(f"The highest score in the class is: {score}")

count = 0

# for i in range(1, 101):
#     count = sum(i)
#     print(i)

# for n in range(1, 11, 3):
#     count = sum(n)
#     print(n)

# for number in range(1, 101):
#     count += number
# print(count)

# count = 0
# for even_number in range(1, 101):
#     if even_number % 2 == 0:
#         count += even_number
# print(count)

# count = 0
# for even_number in range(2, 101, 2):
#     count += even_number
# print(count)

#FizzBuzz gaming test.

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Password generator project.
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like? \n "))
nr_numbers = int(input("How many numbers would you like? \n "))

password = ""

for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

random_password = list(password)
random.shuffle(random_password)
shuffled_password = ""

for char in random_password:
    shuffled_password += char

print(shuffled_password)