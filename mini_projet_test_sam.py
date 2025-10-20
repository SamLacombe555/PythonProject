def afficher_jeu(board):
    for ligne in board:
        print(ligne)
board = [

    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"]

]

liste_solution = ["_", "_", "_", "_"]

def assign_couleurs(board, round):
    for i in range(4):
        choix = int(input(f"Sélectionne la couleur n-{i}"))
        if choix == 0:
            choix_c = "J"
        elif choix == 1:
            choix_c = "B"
        elif choix == 2:
            choix_c = "R"
        elif choix == 3:
            choix_c = "V"
        elif choix == 4:
            choix_c = "O"
        elif choix == 5:
            choix_c = "N"

        board[round-1][i] = choix_c
    return board


def choisir_solution():
    for i in range(4):
        choix = int(input(f"Sélectionne la couleur n-{i}"))
        if choix == 1:
            choix_c = "J"
        elif choix == 2:
            choix_c = "B"
        elif choix == 3:
            choix_c = "R"
        elif choix == 4:
            choix_c = "V"
        elif choix == 5:
            choix_c = "O"
        elif choix == 6:
            choix_c = "N"




def menu_couleurs():

    print ("1 - Jaune")
    print ("2 - Bleu")
    print ("3 - Rouge")
    print ("4 - Vert")
    print ("5 - Orange")
    print ("6 - Noir")
    print ("7 - Mauve")
    print ("8 - Turquoise")
    print ("9 - Gris")

round = 1