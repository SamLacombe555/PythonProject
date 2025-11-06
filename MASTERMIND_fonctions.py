"""
JOUEUR versus CPU : Là, c'est le programme qui explique au joueur décodeur combien de pions rouges/blancs qu'il a.
JOUEUR versus JOUEUR : Ici, c'est le joueur codificateur qui doit réfléchir et taper combien de pions rouges/blancs qu'il reste au joueur décodeur, MAIS on a
une fonction qui détecte s'il a tapé par accident le mauvais nombre de pions rouges/blancs, et le programme le lui dit jusqu'a temps qu'il tape le bon nombre de pions.
"""

# FONCTIONS:

# intro_menu_choix_joueurs(): Fait apparaître le menu du jeu.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer le titre et les choixs du menu
# Fin

# comment_jouer(): Fait apparaître le tutoriel du jeu.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer le tutoriel
# Fin

# ordinateur_solution(): Génère une solution au hazard.
# Entrées: liste_solution (vide)
# Sorties: liste_solution
# Début:
#   Boucle qui génère une liste à 4 couleurs.
#   Retourner la fonction
# Fin

# menu_couleurs(): Fait apparaître le choix de combinaison de couleurs.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer les choixs (J, B, R, V, O, N, M, T, G)
# Fin

# verification_liste(): Vérifie si l'utilisateur a inséré des entrées valides pour la liste.
# Entrées: liste_solution
# Sorties: True ou False
# Début:
#   S'il y a autre chose que les lettres acceptées, retourner un message d'erreur et False.
# Fin

import time, random

round = 1
liste_solution = ["_", "_", "_", "_"]
liste_couleurs = ['J', 'B', 'R', 'V', 'O', 'N', 'M', 'T', 'G']
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
liste_solution = ["_", "_", "_", "_"]

def afficher_jeu(board_j1):
    for ligne in board_j1:
        print(ligne)

def assign_couleurs(board, round):
    """
    Fonction qui modifie le board du décodeur avec ses choix de couleurs
    :param board: Board du décodeur avec ses devinettes
    :param round: Le nombre de ronde jouer par le décodeur
    :return: Le nouveau board avec la devinette du décodeur
    """
    for i in range(4):
        choix = input(f"Décidez quelle sera la {i+1}e couleur :")
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

def intro_menu_choix_joueurs():
    """
    Cette fonction fait apparaître le menu du jeu.
    :return:
    """
    print(r"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━				    
     ███    ███  █████  ███████ ████████ ███████ ██████  ███    ███ ██ ███    ██ ██████  
     ████  ████ ██   ██ ██         ██    ██      ██   ██ ████  ████ ██ ████   ██ ██   ██ 
     ██ ████ ██ ███████ ███████    ██    █████   ██████  ██ ████ ██ ██ ██ ██  ██ ██   ██ 
     ██  ██  ██ ██   ██      ██    ██    ██      ██   ██ ██  ██  ██ ██ ██  ██ ██ ██   ██ 
     ██      ██ ██   ██ ███████    ██    ███████ ██   ██ ██      ██ ██ ██   ████ ██████
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
      """)
    time.sleep(1)
    print("-" * 10)
    print("1 - JOUEUR versus CPU")
    print("2 - JOUEUR versus JOUEUR")
    print("3 - Comment jouer")
    print("-" * 10)
    print("Veuillez taper un chiffre entre 1 et 3, et ensuite Entrée.")

def comment_jouer():
    """
    Cette fonction fait apparaître le tutoriel du jeu.
    :return:
    """
    print("-" * 10)
    print("Le but de ce jeu est de deviner correctement une combinaison de 4 couleurs.\nUn joueur (le codificateur) decide quelle sera la combinaison gagnante, et un deuxième joueur (le décodeur) tente de la trouver par essai-erreur.\nSi une couleur est correctement devinée une couleur, un pion blanc est placé.\nSi une couleur est devinée et qu'en plus elle est placée à la bonne position, un pion rouge est placé.\n12 essais en tout sont permis.")
    print("-" * 10)
    input(print("Veuillez taper Entrée pour retourner au menu."))

def choisir_solution(liste_solution):
    """
    Cette fonction permet de choisir la combinaison de 4 couleurs avec l'aide de la liste en menu_couleurs().
    :param liste_solution:
    :return:
    """
    for i in range(4):
        choix = input(f"Décidez quelle sera la {i+1}e couleur :")
        if choix == '1':
            choix_c = "J"
        elif choix == '2':
            choix_c = "B"
        elif choix == '3':
            choix_c = "R"
        elif choix == '4':
            choix_c = "V"
        elif choix == '5':
            choix_c = "O"
        elif choix == '6':
            choix_c = "N"
        elif choix == '7':
            choix_c = "M"
        elif choix == '8':
            choix_c = "T"
        elif choix == '9':
            choix_c = "G"
        else:
            break

        liste_solution[i] = choix_c
    return liste_solution

def menu_couleurs():
    """
    Cette fonction fait apparaître le choix de combinaison de couleurs.
    :return:
    """
    print ("1 - Jaune")
    print ("2 - Bleu")
    print ("3 - Rouge")
    print ("4 - Vert")
    print ("5 - Orange")
    print ("6 - Noir")
    print ("7 - Mauve")
    print ("8 - Turquoise")
    print ("9 - Gris")

def ordinateur_solution():
    """
    Cette fonction génère une solution au hazard.
    :return:
    """
    liste_solution = []
    for i in range(4):
        i = random.choice(liste_couleurs)
        liste_solution.append(i)
    return liste_solution

def verification_liste(liste_solution):
    """
    Cette fonction vérifie si l'utilisateur a inséré des entrées valides pour la liste.
    :param liste_solution:
    :return:
    """
    if '_' in liste_solution:
        print("Votre liste est invalide. Veuillez redémarrer le programme et réessayer.")
        return False

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
    # Si ça retourn 0, le jeux n'es