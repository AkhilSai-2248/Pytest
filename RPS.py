#!/usr/bin/python3
import random
game_list = ['rock','paper','Scissors']
computer = c = 0
command = p = 0
print("Score: Computer" + str(c) + "Player" + str(p))
# for loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Rock,paper,scissors or Quit:")
    if command == computer_choice:
        print("Tie")
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print("Player Won!")
            p += 1
        else:
            print("Computer Won!")
            c += 1
    elif command == 'Paper':
        if command == 'Rock':
            print("Computer won!")
            p += 1
        else:
            print("Computer Won!")
            p += 1 
    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print("Computer Won!")
            p += 1
        else:
            print("Computer Won!")
            c =+ 1
    elif command == 'Quit':
        break
    else:
       print("Wrong Command!")
    print("Player:"+ str(command))
    print("Computer:" + str(computer_choice))
    print("")
    print("Score: Computer"+ str(c) + "Player" + str(p))
    print("")
    