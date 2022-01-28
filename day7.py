import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Psst, the solution is {chosen_word}.")

word_length = len(chosen_word)

display = []  # setup an empty list
for _ in range(word_length):
    display.append("_")


print("Welcome to the Hangman Game!\n")

while 1 > 0:
    guess = input("Please guess a letter. ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
