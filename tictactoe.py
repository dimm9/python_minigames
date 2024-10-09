field = "| | | |\n| | | |\n| | | |"
#0 - 1; 1 - 3; 2 - 5; 3 - 9; 4 - 11; 5 - 13; 6 -17; 7- 19; 8 - 21
indices = {0: 1, 1: 3, 2: 5, 3: 9, 4: 11, 5: 13, 6: 17, 7: 19, 8: 21}

x = 'X'
o = 'O'
gameOver = False
tie = False


def create_field():
    print(field)


def player_move(name):
    global field
    global indices
    valid_move = False
    while not valid_move:
        coords = int(input("Player " + name + ":(0-8) "))
        if 8 >= coords >= 0:
            if field[indices[coords]] == ' ':
                field_list = list(field)
                field_list[indices[coords]] = name
                field = ''.join(field_list)
                valid_move = True
                check_win()
            else:
                print("The place is already taken! Try again.")
        else:
            print("Index is too high or too low")


def check_win():
    global gameOver
    global tie
    if field[1] == field[3] == field[5] != ' ':
        gameOver = True
        print("Player " + field[1] + " won")
    elif field[9] == field[11] == field[13] != ' ':
        gameOver = True
        print("Player " + field[9] + " won")
    elif field[17] == field[19] == field[21] != ' ':
        gameOver = True
        print("Player " + field[17] + " won")
    elif field[1] == field[9] == field[17] != ' ':
        gameOver = True
        print("Player " + field[17] + " won")
    elif field[3] == field[11] == field[19] != ' ':
        gameOver = True
        print("Player " + field[11] + " won")
    elif field[5] == field[13] == field[21] != ' ':
        gameOver = True
        print("Player " + field[5] + " won")
    elif field[1] == field[11] == field[21] != ' ':
        gameOver = True
        print("Player " + field[11] + " won")
    elif field[5] == field[11] == field[17] != ' ':
        gameOver = True
        print("Player " + field[11] + " won")

    inc = 0
    for i in field:
        if i == ' ':
            inc += 1

    if inc == 0 and not gameOver:
        print("Its a tie!")
        tie = True


def main():
    print("Game started")
    while not gameOver:
        player_move(x)
        create_field()
        if gameOver: break
        player_move(o)
        create_field()
        print("-----------------")
main()

