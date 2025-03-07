import colorama

from colorama import Fore, Style

colorama.init(autoreset=True)

# Spielfeld initialisieren (6 Zeilen, 7 Spalten)

board = [[" " for _ in range(7)] for _ in range(6)]

# Spieler-Definitionen mit Farben

PLAYERS = {

    1: Fore.BLUE + "O" + Style.RESET_ALL,

    2: Fore.YELLOW + "X" + Style.RESET_ALL,

}

def print_board():

    """ Gibt das Spielfeld aus. """

    for row in board:

        print("|" + "|".join(row) + "|")

    print(" 1 2 3 4 5 6 7 ")  # Spaltennummern

def play_one_round(player):

    """ Lässt einen Spieler einen Zug machen. """

    while True:

        spalte = input(f"Spieler {player} ({PLAYERS[player]}), wähle eine Spalte (1-7): ")

        if spalte.isdigit():  

            spalte = int(spalte) - 1  

            if 0 <= spalte < 7:  

                for zeile in range(5, -1, -1):  

                    if board[zeile][spalte] == " ":

                        board[zeile][spalte] = PLAYERS[player]

                        return  

                print("Spalte voll! Wähle eine andere.")

            else:

                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 7 eingeben.")

        else:

            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

def check_winner(player):

    """ Überprüft, ob der aktuelle Spieler gewonnen hat. """

    symbol = PLAYERS[player]

    # Horizontale Prüfung

    for zeile in range(6):

        for spalte in range(4):

            if all(board[zeile][spalte + i] == symbol for i in range(4)):

                return player

    # Vertikale Prüfung

    for zeile in range(3):

        for spalte in range(7):

            if all(board[zeile + i][spalte] == symbol for i in range(4)):

                return player

    # Diagonal (↘)

    for zeile in range(3):

        for spalte in range(4):

            if all(board[zeile + i][spalte + i] == symbol for i in range(4)):

                return player

    # Diagonal (↙)

    for zeile in range(3, 6):

        for spalte in range(4):

            if all(board[zeile - i][spalte + i] == symbol for i in range(4)):

                return player

    return None

def reset_board():

    """ Setzt das Spielfeld zurück. """

    global board

    board = [[" " for _ in range(7)] for _ in range(6)]

# Hauptspiel-Loop

while True:

    reset_board()

    player = 1

    winner = None

    while not winner:

        print_board()

        play_one_round(player)

        winner = check_winner(player)

        if winner:

            print_board()

            print(f"Spieler {winner} ({PLAYERS[winner]}) hat gewonnen! ")

            break

        player = 3 - player  # Wechselt zwischen 1 und 2

    nochmal = input("Möchtest du noch eine Runde spielen? (1 = Ja, 2 = Nein): ")

    if nochmal != "1":

        print("Danke fürs Spielen!")

        break 