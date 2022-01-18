import random
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

print("Welcome to Rock, Paper, Scissors!")
print("You will play against the computer by choosing:\n 'Rock', 'Paper', or 'Scissors'.")
choice = input("\nWhat is your choice?\n").lower()

if choice == "rock":
    print(rock)
    print("\n Your choice.")
elif choice == "paper":
    print(paper)
    print("\n Your choice.")
elif choice == "scissors":
    print(scissors)
    print("\n Your choice.")

computer = random.randint(1, 3)
if computer == 1:
    print(rock)
    computer_choice = "rock"
    print("\n Computer's choice.")
elif computer == 2:
    computer_choice = "paper"
    print(paper)
    print("\n Computer's choice.")
elif computer == 3:
    computer_choice = "scissors"
    print(scissors)
    print("\n Computer's choice.")


if choice == computer_choice:
    print("\nIt's a draw! Try again.")
if (choice == "rock") and (computer_choice == "scissors"):
    print("You win!!!")
if (choice == "scissors") and (computer_choice == "rock"):
    print("You lose!!!")
if (choice == "scissors") and (computer_choice == "paper"):
    print("You win!!!")
if (choice == "paper") and (computer_choice == "scissors"):
    print("You lose!!!")
if (choice == "paper") and (computer_choice == "rock"):
    print("You win!!!")
if (choice == "rock") and (computer_choice == "paper"):
    print("You lose!!!")
