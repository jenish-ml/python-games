name = input("Enter your name: ")
print(f'Hello {name}! Welcome to the game!')

game = input(f'Do you want to play (y/n)?: ').lower()

if game == 'y' or game == 'yes':
    print("Let's play!")
    
    ready = input("Find the Mine. Are you ready (y/n)?: ").lower()
    if ready == 'y' or ready == 'yes':
        print("Start the game!")

        move = input("Do you want to move right or left (r/l)?: ").lower()
        if move == 'l' or move == 'left':
            print("Yaa you are safe. You see a river and a bridge.")
            
            path = input("Do you want to move to the river or the bridge (r/b)?: ").lower()
            if path == 'b' or path == 'bridge':
                print("Yaa you are safe. You see a house and a church.")
                
                place = input("Do you want to move to the house or the church (h/c)?: ").lower()
                if place == 'c' or place == 'church':
                    print("Yaa you are safe. You see a river and a bridge again.")
                    
                    path2 = input("Do you want to move to the river or the bridge (r/b)?: ").lower()
                    if path2 == 'b' or path2 == 'bridge':
                        print("Yaa you are safe. You see a house and a church.")
                        
                        place2 = input("Do you want to move to the house or the church (h/c)?: ").lower()
                        if place2 == 'c' or place2 == 'church':
                            print("Congratulations! You found the mine. You win!")
                        else:
                            print("The family members in the house kill you. You lose!")
                    else:
                        print("The hidden alligator kills you. You lose!")
                else:
                    print("The family members in the house kill you. You lose!")
            else:
                print("The hidden alligator kills you. You lose!")
        else:
            print("You fall into a hole. You lose!")
    else:
        print("Game aborted. Bye!")
else:
    print("Bye! See you next time.")
