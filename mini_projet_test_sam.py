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

def assign_couleurs(board, r):
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
            
        board[r-1][i] = choix_c

def choisir_solution():




def menu_couleurs():

    print ("0 - Jaune")
    print ("1 - Bleu")
    print ("2 - Rouge")
    print ("3 - Vert")
    print ("4 - Orange")
    print ("5 - Noir")

round = 1