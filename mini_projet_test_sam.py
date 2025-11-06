def afficher_jeu(board_j1):
    for ligne in board_j1:
        print(ligne)
board = [

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
    """
    Fonction qui corrige la devinette du decodeur
    :param board_j1: Le board que le décodeur peut voir et joue avec
    :param liste_solution: La combinaison solution du codificateur
    :return: Nouveau board contenant la devinette du décodeur et la correction du codificateur
    """
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


# board_check definé vide
# board_check.append(board[round-1][0]) de 0 à 3
# if board_check == liste_solution
    # return False
# elif round == 13:
    # return False
# else:
    # return True

def verifier_fin(board, liste_solution):
    """
    Fonction qui vérifie si le jeux est fini
    :param board: Le board qu'on joue avec
    :param liste_solution: La solution du codificateur
    :return: La fin ou continuation du jeux
    """
    board_check = []
    for k in range(4):
        board_check.append(board[round-1][k])
    if board_check == liste_solution:
        return 1
    else:
        round +=1
        if round == 13:
            return 2
        else:
            return 0
    # Si ça retourne 1, le décodeur a gagné
    # Si ça retourne 2, le décodeur a perdu
    # Si ça retourn 0, le jeux n'est pas terminé et ça recommence






while win_condition == 0:
    # boucle du jeux

    win_condition = verifier_fin(board,liste_solution)
if win_condition == 1:
    print("win") # victoire
elif win_condition == 2:
    print("lose") # défaite