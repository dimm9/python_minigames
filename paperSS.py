import random

options = ("R", "P", "S")

running = True

while running:

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Choose your option: 🪨  - R, 📜 - P, ✂️ - S: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "R" and computer == "S":
        print("You win;)")
    elif player == "P" and computer == "R":
        print("You win;)")
    elif player == "S" and computer == "P":
        print("You win;)")
    else:
        print("Game over:(")

    new_game = input("Play again(Y/N)?").upper
    if new_game == "Y":
        running = True

    if new_game == "N":
        running = False
        break

print("Thanks for the game!")


