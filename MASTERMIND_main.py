from MASTERMIND_fonctions import *

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
    boucle:
        fonction qui print la table de jeu 
        fonction qui print les choix de couleurs du décodeur 
        fonction qui modifie la table de jeux accordement avec les choix du décodeur
        fonction qui corrige la table de jeux accordement avec la solution choisi par le codificateur
        fonction qui vérifie si le jeu est terminé et qui terminera la boucle 
        ajouter 1 au comptage de rond 
    fonction qui print la table de jeu 
    si le jeu fini car le décodeur a gagné:
        print espace
        print que le décodeur à gagné avec telle essay
    sinon, si le jeu fini car le décodeur a perdu:
    print que le décodeur a perdu
"""

import time

round = int(1) #le comptage du rond courant
liste_solution = ["_", "_", "_", "_"]
liste_couleurs_random = ['J', 'B', 'R', 'V', 'O', 'N', 'M', 'T', 'G']
liste_couleurs = ['J', 'B', 'R', 'V', 'O', 'N', 'M', 'T', 'G']

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
win_condition = 0 #condition de victoire

if __name__ == "__main__":

    while True:
        intro_menu_choix_joueurs()
        choix = input()
        if choix == "1":
            liste_solution = ordinateur_solution(liste_couleurs_random)
            nom_decodeur = "Le décodeur"
            break
        elif choix == "2":
            nom_codificateur = str(input("Qui sera le joueur codificateur? Veuillez taper son nom, et ensuite Entrée."))
            nom_decodeur = str(input("Qui sera le joueur décodeur? Veuillez taper son nom, et ensuite Entrée."))
            print(f"{nom_decodeur}, veuillez vous retourner et ne pas regarder l'écran.")
            time.sleep(5)
            print(f"{nom_codificateur}, en vous servant du menu suivant, veuillez choisir une solution composée d'une combinaison de 4 couleurs.")
            menu_couleurs()
            choisir_solution(liste_solution)
            print(liste_solution)
            if not verification_liste(liste_solution):
                break
            print("Cette liste est-elle correcte? Répondez avec O ou N.")
            input_verification = input()
            if input_verification == 'N':
                print(r"Tant pis ¯\_(ツ)_/¯. Veuillez recommencer depuis le début.")
                time.sleep(3)
            elif input_verification == 'O':
                print("\n" * 20)
                print(nom_decodeur + ", vous pouvez à présent regarder l'écran.")
                time.sleep(5)
                break
            else:
                print("Mauvaise entrée.")
        elif choix == "3":
            comment_jouer()

    while win_condition == 0:
        afficher_jeu(board)
        menu_couleurs()
        board = assign_couleurs(board, round)
        board = j2_verifie(board, liste_solution, round)
        win_condition = verifier_fin(board, liste_solution, round)
        round += 1
    afficher_jeu(board)
    if win_condition == 1:
        print("-" * 10)
        print(f"{nom_decodeur} a gagné en {round} essais!")
    elif win_condition == 2:
        print(f"Perdu. La solution était {liste_solution}")
    print("Rejouer? O/N")


