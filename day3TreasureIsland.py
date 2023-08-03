# height = int(input("Enter your height in cm? "))
# bill = 0

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Please pay $5.")
#     elif age <= 18:
#         bill = 7
#         print("Please pay $7.")
#     elif age >= 45 and age <= 55:
#         bill = 0
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Please pay $12.")

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y" or "y":
#         bill += 3
#     else:
#         bill = bill
#     print(f"Your final bill is ${bill}.")
    
# else:
#     print("Sorry, you have to grow taller before you can ride.")


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

# Love Calculator Exercise.
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# name = name1.lower() + name2.lower()

# true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
# love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

# resultString = str(true) + str(love)

# loveScore = int(resultString)

# if loveScore < 10 or loveScore > 90:
#     print(f"Your love score is {loveScore}, you go together like coke and mentos.")
# elif loveScore >= 40 and loveScore <= 50:
#     print(f"Your love score is {loveScore}, you are alright together.")
# else:
#     print(f"Your score is {loveScore}.")


print("Bem vindo a sua historia interativa! aqui voce é o protagonista e deve salvar o reino do temivel Feiticeiro de Jade! Boa sorte, voce vai precisar!")
print()
print()
print()
print("Seja bem vindo bravo guerreiro, você é um dos ultimos Samurais encarregado pelo lorde Yashida de encontrar um valioso tesouro que poderá enfim trazer a paz ao reino libertando a todos do cruel e impiedoso Feiticeiro de Jade.")

print()

print("Depois da terrível encosta negra do pantano da maldade a entrada de uma caverna assombrosa desponta ao horizonte, após uma longa viajem você chegou ao covil do temivel feiticeiro.")

print()

print("O cheiro de enxofre banha o ar e nenhum luz parece sobreviver as trevas conforme seus passos te aproximam de seu terrível destino. Subito, ao beirar a entrada da caverna, uma horda de grandes Morcegos saem da caverna com suas asas farfalhantes e gritos agudos.")

print()

print("Recuperado do susto, você adentra a escuridão desconhecida da caverna, um longo e escuro caminho se estende a sua frente!")

print()

print('Você deve acender uma "tocha" caso não o faça você poderá andar a devira pelo escuro')

answer = input('o que você deseja fazer "Acender" ou "Caminhar"?\n').lower()

if answer != "acender":
    print("Você tropeça em uma pedra e cai em um buraco sem fim, você morreu e todo reino foi destruído pelo maligno Feiticeiro de Jade!")
elif answer == "acender":
    print("Você acende a tocha e segue seu caminho, após um longo tempo você chega a uma bifurcação, a sua esquerda uma porta de pedra, a sua direita uma passagem escura, qual caminho você deseja seguir?")
    answer = input('Escolha "Esquerda" ou "Direita"\n').lower()
    if answer != "direita":
        print("Você segue pela porta de pedra e se depara com uma sala com um grande baú de madeira, ao se aproximar do baú, uma armadilha é ativada e você é esmagado por uma pedra gigante, você morreu e todo reino foi destruído pelo maligno Feiticeiro de Jade!")
    elif answer == "direita":
        print("Ao seguir o caminho da direita você chega ao que parece ser uma escada que sobe de um profundo poço escuro, você sente o ar gélido subir da escuridão e então juntando toda coragem que lhe resta você desce pela longa escada chegando a um grande salão, nos qual outras 3 portas se encontram, uma de madeira, uma de ferro e uma de pedra.")
        answer = input('Por qual porta deseja passar\n').lower()
        if answer != "ferro":
            print("Ao abrir a porta milhares de flechas são disparadas em sua direção, você morreu e todo reino foi destruído pelo maligno Feiticeiro de Jade!")
        elif answer == "ferro":
            print("Você atravessa por um grande e luxuoso corredor chegando a uma camara dourada, no centro da camara você vê um grande baú de ouro, ao se aproximar do baú, uma voz tenebrosa ecoa por todos os lados, o Feiticeiro de Jade surge em sua frente e diz: \n- Você é um guerreiro corajoso, mas não é páreo para mim, você morrerá aqui e todo reino será destruído!")