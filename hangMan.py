import random  

word_list = ["ardvark", "baboon", "camel"]  # Uma variavel tipo "lista" contendo as palavras a serem utilizadas no jogo.

chosen_word = random.choice(word_list)

display = []    #Display é uma variavel tipo lista que recebera o caracteres que formarão a palavras escolhida na variavel chosen_word. 

print(f"The solutiom word is {chosen_word}")

guess = input("Guess a letter: ").lower()

word_lenght = chosen_word   # Uma variavel tipo primitiva usada para receber o valor da variavel chosen_word.

# O primeiro loop for itera sobre a variavel word_lenght separando cada caracter da varavel letter.
for letter in word_lenght:  
    display += "_"

# O segundo loop for pega a posição de cada caracter usando como base o valor "tamanho" da variavel word_lenght.
for position in range(len(word_lenght)): 
    letter = word_lenght[position]
    if letter == guess:
        display[position] = letter

print(display)