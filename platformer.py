import colorama
from colorama import Fore, Style
import os
import time

colorama.init()
quitQ = False

xp = 0
sp = 0
lvl = 0
name = "Bob"
stats = {xp, sp, lvl, name}

def refresh():
    os.system('cls' if os.name == 'nt' else 'clear')

def save():
    global stats
    file = open("game.txt", "w")
    for i in stats:
        file.write(str(i) + "\n")
    print("...Progress saved!")
    file.close()

def load_game():
    global stats, xp, sp, lvl, name
    file = open("game.txt", "r")
    loadALL = file.readlines()
    xp = loadALL[0]
    sp = loadALL[1]
    lvl = loadALL[2]
    name = loadALL[3]
    start_game(xp, sp, lvl, name)
    print("Welcome back, " + name + "!")
    file.close()

def draw_menu():
    print(Fore.CYAN + "The Edge of Oblivion: Demo" + Style.RESET_ALL)
    print(Fore.CYAN + "----------------" + Style.RESET_ALL)
    print(Fore.CYAN + "1 - PLAY" + Style.RESET_ALL)
    print(Fore.CYAN + "2 - LOAD" + Style.RESET_ALL)
    print(Fore.CYAN + "3 - HELP" + Style.RESET_ALL)
    print(Fore.CYAN + "4 - QUIT" + Style.RESET_ALL)
    print(Fore.CYAN + "----------------" + Style.RESET_ALL)

def start_game(xp, ip, lvl, name):
    pass

def game_loop():
    global quitQ
    while not quitQ:
        draw_menu()
        choice = int(input("> "))
        if choice == 1:
            refresh()
            name = input("Character's name: ")
            start_game(0, 0, 0, name)
            break
        if choice == 2:
            refresh()
            load_game()
        if choice == 3:
            refresh()
            file = open("gamehelp", "r")
            text = file.readlines()
            for line in text:
                print(line.strip())
            file.close()
        if choice == 4:
            print("Do you really want to quit?")
            choice = int(input("(Y/N) "))
            if choice == 1:
                save()
            quitQ = True

def main():
    game_loop()

main()