import random

rock = '''
       _______
    --'   ____)
         (_____)
         (_____)
          (____)
    -. __ (___)
    '''
paper = '''
        _______
    ---'   ____)___
            _______)
            _______)
            _______)
    ---.__________)
    '''
scissors = '''
        ______
    ---'   ____)___
            _______)
        ___________)
          (____)
    ---.__(___)
    '''

game_images = [rock, paper, scissors]

player1 = int(input("What do your choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))
if player1 >= 3 or player1 < 0:
    print("You typed an invalid number, You lose!\n")
else:
    player2 = random.randint(0, 2)

    print("Player 1 chose: ")
    print(game_images[player1])

    print("Player 2 chose: ")
    print(game_images[player2])

    if player1 >= 3 or player1 < 0:
        print("You typed an invalid number, You lose!\n")
    if player1 == 0 and player2 == 1:
        print("Paper cover Rock, You lose!\n")
    elif player1 == 0 and player2 == 2:
        print("Rock broken Scissor, You win!\n")
    elif player1 == 1 and player2 == 0:
        print("Paper cover Rock, You win!\n")
    elif player1 == 1 and player2 == 2:
        print("Scissor cut Paper, You lose!\n")
    elif player1 == 2 and player2 == 0:
        print("Rock broken Scissor, You lose!\n")    
    elif player1 == 2 and player2 == 1:
        print("Scissor cut Paper, You win!\n")
    else:
        print("It's a draw!\n")
