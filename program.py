print("UPDATED CODE")
import random

stages = [
    "❤️❤️❤️❤️❤️❤️",
    "❤️❤️❤️❤️❤️🤍",
    "❤️❤️❤️❤️🤍🤍",
    "❤️❤️❤️🤍🤍🤍",
    "❤️❤️🤍🤍🤍🤍",
    "❤️🤍🤍🤍🤍🤍",
    "💀"
]

words = ["pen", "car", "phone"]

lives = 6

random_word = random.choice(words)
print(random_word)  # remove this in real game

# create placeholder
placeholder = ""
correct_letter = []

for position in range(len(random_word)):
    placeholder += "_"
print(placeholder)

game_over = False

while not game_over:

    user = input("\nwhat letter you choose?\n").lower()

    display = ""

    for letter in random_word:
        if letter == user:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"   # <-- FIXED (no print here)

    print(display)

    if user not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose")

    if "_" not in display:
        game_over = True
        print("you win")

    print(stages[lives])
def greet():
    print("hello sir!")
    print("how are you??")
    print("do you need something?")

greet()