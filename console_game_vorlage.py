Zeile = 7  
Spalte = 7  

     [' ' for _ in range(7)] for _ in range(7)
 ]

PLAYERS = {1: "O", 2: "X"}

def print_board():
    spielfeld = ""
    for Zeile in board:
        spielfeld += "|".join(Zeile) + "\n"
        spielfeld += "-" * (2 * len(Zeile) - 1) + "\n"
        print(spielfeld)

print_board()

















