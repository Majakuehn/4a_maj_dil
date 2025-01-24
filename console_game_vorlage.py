Zeile = 7
Spalte = 7

board = [
    [' ' for _ in range(Spalte)] for _ in range(Zeile)
]

PLAYERS = {1: "O", 2: "X"}

def print_board():
    spielfeld = ""
    for zeile in board:
        spielfeld += "|".join(zeile) + "\n"
        spielfeld += "-" * (2 * len(zeile) - 1) + "\n"
    print(spielfeld)

def play_one_round(board, player):
    while True:
        user_input = input(f"Player {player} ({PLAYERS[player]}), wähle eine Spalte (1-{Spalte}): ")
        
        if user_input== 
        spalte = int(user_input) - 1
        if spalte < 0 or spalte >= Spalte:
            print(f"Ungültige Spalte. Bitte wähle eine Zahl zwischen 1 und {Spalte}.")
            continue
           






