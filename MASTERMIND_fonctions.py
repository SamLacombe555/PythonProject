
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

# verification_liste(): Vérifie si l'utilisateur à insérer des entrées valides pour la liste.
# Entrées: liste_solution
# Sorties: True ou False
# Début:
#   S'il y a autre chose que les lettres acceptées, retourner un message d'erreur et False.
# Fin

# verifier_fin() : Vérifie si le jeu est fini
# Entrées: board, liste_solution, round
# Sorties: 0, 1 ou 2
# Début:
#   Si la

import time, random



def afficher_jeu(board_j1):
    """
    Fonction qui affiche la table de jeu
    :param board_j1: La table de jeu
    :return:
    """
    for ligne in board_j1:
        print(ligne)

def assign_couleurs(board, round):
    """
    Fonction qui modifie le board du décodeur avec ses choix de couleurs.
    :param board: Table de jeu du décodeur avec ses devinettes
    :param round: Le nombre de ronds joués par le décodeur
    :return: La nouvelle table de jeu avec la devinette du décodeur
    """
    for i in range(4):
        deux_couleurs = True
        while deux_couleurs == True:
            choix = int(input(f"Décidez quelle sera la {i+1}e couleur :"))
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
            else:
                choix_c ="_"

            if choix_c == "_":
                print("Veuillez entrer un choix valide.")
                deux_couleurs = True
            elif choix_c in board[round-1]:
                print("La solution ne contient pas deux fois la même couleur.")
                deux_couleurs = True
            else:
                board[round-1][i] = choix_c
                deux_couleurs = False
    return board

def intro_menu_choix_joueurs():
    """
    Cette fonction fait apparaître le menu du jeu.
    :return:
    """
    # Réf: https://patorjk.com/
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
    :param liste_solution: la solution qui sera choisie par le codificateur
    :return: la solution choisie par le codificateur
    """
    for i in range(4):
        deux_couleurs = True
        while deux_couleurs == True:
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

            if choix_c in liste_solution:
                print("La solution ne peut pas contenir deux fois la même couleur.")
                deux_couleurs = True
            else:
                liste_solution[i] = choix_c
                deux_couleurs = False

    return liste_solution

def menu_couleurs():
    """
    Cette fonction fait apparaître le choix de combinaison de couleurs.
    :return:
    """
    print("-" * 10)
    print ("1 - Jaune")
    print ("2 - Bleu")
    print ("3 - Rouge")
    print ("4 - Vert")
    print ("5 - Orange")
    print ("6 - Noir")
    print ("7 - Mauve")
    print ("8 - Turquoise")
    print ("9 - Gris")
    print("-" * 10)

def ordinateur_solution(liste_couleurs_random):
    """
    Cette fonction génère une solution au hasard.
    :param liste_couleurs_random: la liste de couleurs qui peuvent être choisi par hasard
    :return: solution générée par hasard
    """
    liste_solution = []
    for i in range(4):
        i = random.choice(liste_couleurs_random)
        liste_solution.append(i)
        liste_couleurs_random.remove(i)
    return liste_solution

def verification_liste(liste_solution):
    """
    Cette fonction vérifie si l'utilisateur à insérer des entrées valides pour la liste.
    :param liste_solution: la solution que le décodeur doit deviner
    :return: si non-valide, il l'annonce au joueur et au programme
    """
    if '_' in liste_solution:
        print("Votre liste est invalide. Veuillez redémarrer le programme et réessayer.")
        return False

def j2_verifie(board, liste_solution, round):
    """
    Fonction qui corrige la devinette du decodeur
    :param board: La table du jeu que le décodeur peut voir et joue avec
    :param liste_solution: La combinaison solution du codificateur
    :param round: Le rond du jeu
    :return: Nouvelle table de jeu contenant la devinette du décodeur et la correction du codificateur
    """
    count_rouge = 0 #le nombre de bonnes couleurs au bon endroit
    count_blanc = 0 #le nombre de bonnes couleurs dans le mauvais endroit
    for i in range(4):
        if board[round-1][i] in liste_solution:
            if i == liste_solution.index(board[round-1][i]):
                count_rouge += 1
            else:
                count_blanc += 1
    board[round-1].append(f"{count_rouge} rouge(s), {count_blanc} blanc(s)")
    return board

def verifier_fin(board, liste_solution, round):
    """
    Fonction qui vérifie si le jeu est fini
    :param board: La table du jeu qu'on joue avec
    :param liste_solution: La solution du codificateur
    :param liste_solution: Le rond du jeux
    :return: La fin ou continuation du jeu
    """
    board_check = [] #board temporaire contenant seulement la ligne horizontale correspondant au round
    for k in range(4):
        board_check.append(board[round-1][k])
    if board_check == liste_solution:
        return 1
    elif round == 12:
        return 2
    else:
        return 0
    # Si ça retourne 1, le décodeur a gagné
    # Si ça retourne 2, le décodeur a perdu
    # Si ça retourn 0, le jeu n'est pas terminé