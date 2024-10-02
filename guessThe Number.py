import random
name = input("Enter your name: ")
print(f'Hello {name}! Welcome to the game!')
game = input(f'Do you want to play(y/n)?: ').lower()

play = game == 'yes' or game == 'y'

if play:
    print("Let's play!")
    print("I am thinking of a number between 1 and 10. Can you guess it?")
    number = random.randint(1, 10)
    guess = int(input("Enter your guess: "))
    while guess != number:
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Enter your guess: "))
    print("Correct! You win!")
else:
    print("Bye! See you next time!")