from MASTERMIND_fonctions import *

"""
A DOCUMENTER (SAM)

afficher_jeu()
assign_couleurs()

ligne
board_j1 (liste)
board_j2 (liste)
j2_verifie
board
nouveau_board
round
count_rouge
rouges
count_blanc
blancs

+ PSEUDOCODE

"""

# - PSEUDOCODE

# Entrées:
# nom_codificateur (str): Nom du joueur codificateur
# nom_decodeur (str): Nom du joueur décodeur
# choix/choix_c: L'entrée pour les différents menus de sélection. S'identifie par un chiffre

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
win_condition = 0

if __name__ == "__main__":

    while True:
        intro_menu_choix_joueurs()
        choix = input()
        if choix == "1":
            liste_solution = ordinateur_solution()
            break
        elif choix == "2":
            nom_codificateur = str(input("Qui sera le joueur codificateur? Veuillez taper son nom, et ensuite Entrée."))
            nom_decodeur = str(input("Qui sera le joueur décodeur? Veuillez taper son nom, et ensuite Entrée."))
            print(nom_decodeur + ", veuillez vous retourner et ne pas regarder l'écran.")
            time.sleep(5)
            print(nom_codificateur + ", en vous servant du menu suivant, veuillez choisir une solution composée du combinaison de 4 couleurs.")
            menu_couleurs()
            choisir_solution(liste_solution)
            print(liste_solution)
            if verification_liste(liste_solution) == False:
                break
            print("Cette liste est-elle correcte? Répondez avec O ou N.")
            input_verification = input()
            if input_verification == 'N':
                print(r"Tant pis ¯\_(ツ)_/¯. Veuillez recommencer depuis le début.")
                time.sleep(3)
            elif input_verification == 'O':
                break
            else:
                print("Mauvaise entrée.")
        elif choix == "3":
            comment_jouer()

    afficher_jeu(board)
    assign_couleurs(board, round)

