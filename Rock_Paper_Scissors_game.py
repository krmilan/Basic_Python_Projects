rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

list = [rock,paper,scissors]

choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >=3 or choice < 0:
    print("You typed an invalid number, You lose!")
else:
    print(list[choice])

    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(list[computer_choice])
      
      
    if choice == 0 and computer_choice == 1:
        print("You lose!")
    elif choice == 1 and computer_choice == 2:
        print("You lose!")
    elif choice == 2 and computer_choice == 0:
        print("You lose!")
    elif choice == computer_choice:
        print("Its a draw")
    else:
        print("You win!")
