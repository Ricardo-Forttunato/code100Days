import math

#     # Syntax de uma função:
# def greet():
#     print(f"Hello! Ricardo")
#     print("This is may first program!")
#     print("Bye!")
#     # Chamando a função:
# greet("Ricardo", {"Fortunato"})

#     # É possivel passar um argumento para a função, para isso utilizamos variaveis dentro do () da função:
# def greet_with_name(nome):
#     print(f"Hello! {nome}")
#     print("This is may first program!")
#     print("Bye!")

#     # Chamando a função:
# greet_with_name("Ricardo")

#     # É possivel usar mais de um parametro em uma função.
# def greet_with(name = input("Input a name: "), location = input("Input a location: ")): # name e location são parametros da função.
#     print(f"Hello {name}.")
#     print(f"What is it like in {location}")

# greet_with() # "Ricardo" e "Brasil" são os valores declarados para os parametros da função.

#    # É possivel usar mais de um parametro em uma função.
# def greet_with(location, name): # name e location são parametros da função.
#     print(f"Hello {name}.")
#     print(f"What is it like in {location}")

# greet_with("Brasil", name = "Ricardo") # É possivel relacionar diretamente um parametro e um argumento diretament na chamada da função.
# #              |-> A posição do argumento depende da posição do parametro dentro da função, o primeiro argumento não precisa ser relacionado por padrão ele é relacionado com o primeiro parametro.

# def paint_calc(height, width, cover):
#     cans_of_paint = math.ceil((height * width) / cover)
#     print(f"You'll need {cans_of_paint} cans of paint.")
    
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

    # Verifica se um numero é primo ou não.
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

prime_checker( int(input("Check this number: ")))

