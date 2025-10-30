def afficher_jeu(board_j1):
    for ligne in board_j1:
        print(ligne)
board_j1 = [

    ["_", "_", "_", "_"], # + liste[0][1]append.str("1 pion et 1 pio")
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

board_j2 = [

    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""]

]

liste_solution = ["_", "_", "_", "_"]

def assign_couleurs(board, round):
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
        elif choix == 7:
            choix_c = "M"
        elif choix == 8:
            choix_c = "T"
        elif choix == 9:
            choix_c = "G"

        board[round-1][i] = choix_c
    return board


def choisir_solution(liste):
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
        elif choix == 7:
            choix_c = "M"
        elif choix == 8:
            choix_c = "T"
        elif choix == 9:
            choix_c = "G"

        liste[i] = choix_c
    return liste



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

#fonction j2 verifie une ligne
    #count_rouge = 0
    #count_blanc = 0
    #for choix in board_j1 du round
        #if choix in solution
            #if index_choix_ligne_j1 == index_choix_solution
                #count_rouge += 1
            #else
                #count_blanc += 1


def j2_verifie(board_j1:list, liste_solution:list):
    count_rouge = 0
    count_blanc = 0
    for i in range(4):
        if board_j1[round-1][i] in liste_solution:
            if i == liste_solution.index(board_j1[round-1][i]):
                count_rouge += 1
            else:
                count_blanc += 1
    nouveau_board = board_j1[round-1].append(f"{count_rouge} rouges, {count_blanc} blancs")
    return nouveau_board



round = 1

