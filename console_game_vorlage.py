import random
import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]




def print_board():
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" 1 2 3 4 5 6 7")  

def print_board():
    erste_zeile = "|" + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|" + board[0][3] + "|" + board[0][4] + "|" + board[0][5] + "|" + board[0][6] + "|" +  board[0][7] +"\n"
    zwischenzeile = "-----------------" + "\n"
    zweite_zeile = "|" + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|" + board[1][3] + "|" + board[1][4] + "|" + board[1][5] + "|" + board[1][6] + board[1][7]+ "|" + "\n"
    dritte_zeile = "|" + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|" + board[2][3] + "|" + board[2][4] + "|" + board[2][5] + "|" + board[2][6] + board[0][7] + "|" + "\n"
    vierte_zeile = "|" + board[3][0] + "|" + board[3][1] + "|" + board[3][2] + "|" + board[3][3] + "|" + board[3][4] + "|" + board[3][5] + "|" + board[3][6] +  board[0][7] +"|" + "\n"
    fünfte_zeile = "|" + board[4][0] + "|" + board[4][1] + "|" + board[4][2] + "|" + board[4][3] + "|" + board[4][4] + "|" + board[4][5] + "|" + board[4][6] +  board[0][7] +"|" + "\n"
    sechste_zeile = "|" + board[5][0] + "|" + board[5][1] + "|" + board[5][2] + "|" + board[5][3] + "|" + board[5][4] + "|" + board[5][5] + "|" + board[5][6] +  board[0][7] +"|" + "\n"
    
    print(erste_zeile + zwischenzeile + zweite_zeile + dritte_zeile + vierte_zeile + fünfte_zeile + sechste_zeile + zwischenzeile)


def play_one_round(board, player):
    while True:
        try:
            spalte = int(input(f"Spieler {player} ({PLAYERS[player]}), gib eine Spalte ein (1-7): "))
            if spalte >= 1 and spalte <= 7:
                spalte -= 1
                for zeile in range(5, -1, -1):
                    if board[zeile][spalte] == " ":
                        board[zeile][spalte] = PLAYERS[player]
                        print (zeile, spalte)
                        return
                print("Spalte voll. Wähle eine andere.")
            else:
                print("Input inkorrekt. Wähle eine Spalte zwischen 1 und 7.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 7 ein.")


def check_winner(board, player):
    symbol = PLAYERS[player]

   
    for zeile in range(6):
        for spalte in range(4):
            if (board[zeile][spalte] == symbol and
                board[zeile][spalte + 1] == symbol and
                board[zeile][spalte + 2] == symbol and
                board[zeile][spalte + 3] == symbol):
                return player

    for zeile in range(3):
        for spalte in range(7):
            if (board[zeile][spalte] == symbol and
                board[zeile + 1][spalte] == symbol and
                board[zeile + 2][spalte] == symbol and
                board[zeile + 3][spalte] == symbol):
                return player

    for zeile in range(3):
        for spalte in range(4):
            if (board[zeile][spalte] == symbol and
                board[zeile + 1][spalte + 1] == symbol and
                board[zeile + 2][spalte + 2] == symbol and
                board[zeile + 3][spalte + 3] == symbol):
                return player

    for zeile in range(3, 6):
        for spalte in range(4):
            if (board[zeile][spalte] == symbol and
                board[zeile - 1][spalte + 1] == symbol and
                board[zeile - 2][spalte + 2] == symbol and
                board[zeile - 3][spalte + 3] == symbol):
                return player

    return None


player = 1
while True:
    print_board()
    play_one_round(board, player)
    winner = check_winner(board, player)

    if winner:
        print_board()
        print(f"Spieler {winner} ({PLAYERS[winner]}) hat gewonnen!")
        break


    player = 1 if player == 2 else 2

        
        
        
