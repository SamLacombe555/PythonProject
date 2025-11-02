# CE PROGRAMME NE FONCTIONNERA PAS TOUT SEUL

# - PSEUDOCODE -

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

# joueur_versus_joueur(): Introduit la section joueur versus joueur.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer l'instruction
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



# Entrées:
# nom_codificateur (str): Nom du joueur codificateur
# nom_decodeur (str): Nom du joueur décodeur
# choix: L'entrée pour les différents menus de sélection. S'identifie par un chiffre

# Sorties:
# liste_solution (liste simple de 4 couleurs entrée par joueur Codificateur ou générée par hazard par la fonction ordinateur_solution()

# Modules:
# Time: Purement pour petit effet esthétique
# Random: Pour générer une liste au hazard dans la fonction ordinateur_solution()

"""
Programme principal:
Définir liste_couleurs

    boucle
        intro_menu_choix_joueurs()
        choix égal input()
        si choix est égal à 1:
            liste_solution égal ordinateur_solution()
            casser la boucle
        si choix est égal à 2:
            nom_codificateur égal str(input())
            nom_decodeur égal str(input())
            joueur_versus_joueur()
            menu_couleurs()
            choisir_solution(liste_solution)
            imprimer(liste_solution)
            si verification_liste(liste_solution) égal Faux:
                casser la boucle
            imprimer("O ou N")
            si input_verification égal N:
                imprimer("Tant pis")
            sinon input_verification égal O:
                break
            sinon:
                print("Mauvaise entrée.")
        si choix est égal à 3:
            comment_jouer()

"""


import time, random

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
    print("------------")
    print("1 - JOUEUR versus CPU")
    print("2 - JOUEUR versus JOUEUR")
    print("3 - Comment jouer")
    print("------------")
    print("Veuillez taper un chiffre entre 1 et 3, et ensuite Entrée.")

def comment_jouer():
    """
    Cette fonction fait apparaître le tutoriel du jeu.
    :return:
    """
    print("Le but de ce jeu est de deviner correctement une combinaison de 4 couleurs.\nUn joueur (le codificateur) decide quelle sera la combinaison gagnante, et un deuxième joueur (le décodeur) tente de la trouver par essai-erreur.\nS'il devine correctement une couleur, un pion blanc est placé.\nS'il devine une couleur et qu'en plus elle est placée a la bonne position, un pion rouge est placé. Il a 12 essais en tout.")
    input(print("Veuillez taper Entrée pour retourner au menu."))


def joueur_versus_joueur():
    """
    Cette fonction introduit la section joueur versus joueur.
    :return:
    """
    print(nom_decodeur + ", veuillez vous retourner et ne pas regarder l'écran.")
    time.sleep(5)
    print(nom_codificateur,", en vous servant du menu suivant, veuillez choisir une solution composée du combinaison de 4 couleurs.")

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

if __name__ == "__main__":

    liste_couleurs = ['J', 'B', 'R', 'V', 'O', 'N', 'M', 'T', 'G']

    while True:
        intro_menu_choix_joueurs()
        choix = input()
        if choix == "1":
            liste_solution = ordinateur_solution()
            break
        elif choix == "2":
            nom_codificateur = str(input("Qui sera le joueur codificateur? Veuillez taper son nom, et ensuite Entrée."))
            nom_decodeur = str(input("Qui sera le joueur décodeur? Veuillez taper son nom, et ensuite Entrée."))
            joueur_versus_joueur()
            menu_couleurs()
            choisir_solution(liste_solution)
            print(liste_solution)
            if verification_liste(liste_solution) == False:
                break
            print("Cette liste est-elle correcte? Répondez avec O ou N.")
            input_verification = input()
            if input_verification == 'N':
                print(r"Tant pis ¯\_(ツ)_/¯")
                time.sleep(3)
            elif input_verification == 'O':
                break
            else:
                print("Mauvaise entrée.")
        elif choix == "3":
            comment_jouer()

"""
# Non-utile

    liste_solution = []

    for i in range(4):
        couleur = str(input(nom_codificateur + ", décidez quelle sera la combinaison de 4 couleurs gagnante. Entrez les couleurs une par une. Entrez la %se couleur." % (i+1)))
        try:
            couleur + 3
        except TypeError:
            print("Erreur")
        liste_solution.append(couleur)
        print(liste_solution)
"""