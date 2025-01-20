
Zeile = 7  
Spalte = 7  


def create_board():
    return [[" " for _ in range(Zeile)] for _ in range(Spalte)]


def display_board(board):
    print("\n  " + "   ".join(str(i+1) for i in range(Zeile)))  # Spaltennummern
    print(" +" + "---+" * Zeile)  # obere Begrenzung
    for row in board:
        print(" | " + " | ".join(Spalte) + " |")  # Zeilen mit Inhalten
        print(" +" + "---+" * Zeile)  # untere Begrenzung
