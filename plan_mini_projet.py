"""
Contenu à retrouver dans vos projets :
-	Pseudocode ou schéma
-	Collections : listes 2D et dictionnaires
-	Conditions
-	Boucles
-	Modules
-	Gestion des exceptions et validation des entrées
-	Fonctions
-	Tests unitaires et plans de tests

5.	Faire le pseudocode ou schémas de l’algorithme.
6.	Écrire les plans de tests.
7.	Programmer l’algorithme et les tests unitaires.
8.	Déboguer, corriger, améliorer le programme.
9.	Remise et présentations du mini projet le jeudi 20 novembre 2025 (5%)
"""

# Mastermind:

# PRÉ-PSEUDO

# Joueur 1 - celui qui doit deviner (décodeur)
# Joueur 2 - celui qui choisi et initialise la combinaison solution (codificateur)
# Ex:
# "Joueur Codificateur, décidez quelle sera la combinaison de 4 couleurs gagnante"
# (Après que Joueur 2 a fait ça, il part, Joueur 1 s'assit, et est prêt à commencer)


# Commence par display une liste vide ([_], [_], [_], [_])
# Console demande à utilisateur quelles couleurs qu'il veut insérer (choisir dans une liste pré-définie de couleurs (a.k.a menu_couleurs))
# Console display les couleurs que l'utilisateur à choisi + pions indicatifs blancs ou rouges

# Ex:
# [rouge], [jaune], [vert], [noir]
# Vous avez 1 pion blanc et 1 pion rouge

# Répéter le processus jusqu'à ce que l'utilisateur gagne ou qu'il épuise tout ses tours (10 tours max)


# ENTRÉES
# - 4 trous x 10 rangées/essais (6 couleurs de billes: J, B, R, V, O, N)
# - 4 trous à deviner (6 couleurs de billes: J, B, R, V, O, N)
#SORTIES
# - 4 trous à réponse (blanc et rouge)
#FONCTIONS
# l = int   # ligne
# c = int   # colonne
# - ls_couleurs = [J, B, R, V, O, N]
# - ls_grille_devinette = [
#    ["_"]["_"],["_"]["_"], "*10"
#   ]
# - menu_couleurs()
    # print "0 - jaune"
    # print "1 - bleu"
    # print "2 - rouge"
    # print "3 - vert"
    # print "4 - orange"
    # print "5 - noir"
# If input not 0-5, print("Entrée invalide, veuillez recommencer") else break

# - choix_couleurs()
    # choix = input int
    # couleur_choisi = ls_couleurs[choix]
    # return couleur_choisi

# - assigne_couleur(couleur_choisi, lj)
    # for i in range(len(ls_grille_devinette[lj])):
        #

# - Liste cachée (a.k.a liste_solution)
    # définir liste cachée vide
    # pour chaque colonne:
        # demande de choisir une couleur à désigner
# -

"""
- ENTRÉES -

couleur_bille (valeurs peuvent être J, B, R, V, O, N) (joueur Décodeur peut en entrer 4 par essai)
liste_solution (liste simple de 4 couleurs entrée par joueur Codificateur)

- VALEURS -
RANGEES_RESTANTES = 10 (-1 à chaque essai)


- LISTES -
liste_2d_vide (liste 4x10 qui sera lentement remplie par joueur Décodeur)

- SORTIES -
pions_indicatifs

- FONCTIONS -
menu_couleurs()
choix_couleurs()


TÂCHES/FONCTIONS POUR CHAQUE MEMBRE:
WILL:
SAM:
"""

def menu_couleurs():
    """

    :return:
    """
    print "0 - Jaune"
    print "1 - Bleu"
    print "2 - Rouge"
    print "3 - Vert"
    print "4 - Orange"
    print "5 - Noir"



if __name__ == "__main__":

liste_solution = []
liste_solution_longeur = 4
while len(liste_solution) < liste_solution_longeur:
    couleur = input("Joueur 2, décidez quelle sera la combinaison de 4 couleurs gagnante. Entrez les couleurs une par une.")
    liste_solution.append(couleur)
    print(liste_solution)
