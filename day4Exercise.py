import random

# if random.randint(0, 1) == 0:
#     print("Heads")
# else:
#     print("Tails")


# head_sentence = [1, 2, 3, 4, 5]
# tail_sentence = [6, 7, 8, 9, 10]

# head_or_tail = random.randint(1, 10)

# if head_or_tail in head_sentence:
#     print("Heads")
# else:
#     print("Tails")

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# # random_name = random.randint(0, len(names) -1)
# random_name = random.choice(names)
# print(f"{random_name} is going to buy the meal today!")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)
# print(dirty_dozen[0][0])
# print(dirty_dozen[1][0])
# print(dirty_dozen[1][1])  

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = position[0]
row =   position[1]

map[int(row)- 1][int(column) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
