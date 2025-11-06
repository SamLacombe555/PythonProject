def afficher_jeu(grille):
    """
    Afficher la grille du tic-tac-toe
    :param grille: grille du jeu
    """
    for ligne in grille:
        print(ligne)

grille = [
    # 0     1   2
    ["_", "_", "_"],    #0
    ["_", "_", "_"],    #1
    ["_", "_", "_"]     #2
]

# choisir x ou o
jeton = input("Voulez-vous x ou o ?")
# boucle pour les tours des joueurs
while True:
    # afficher le jeu
    afficher_jeu(grille)
    print("Tour de", jeton)
    # demander le choix du joueur
    while True:
        l = int(input("Dans quelle ligne tu veux jouer (0,1,2) ? "))
        c = int(input("Dans quelle colonne tu veux jouer (0,1,2) ? "))
        # vérifier que le choix du joueur est valide
        if l in [0, 1, 2] and c in [0, 1, 2] and grille[l][c] == "_":
            break
        else:
            print("Choix non valide.")
    # remplacer le choix du joueur par x ou o dans la grille
    grille[l][c] = jeton
    # vérifier les conditions pour gagner
    fini = False
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != "_":
            afficher_jeu(grille)
            print(grille[i][0], "a gagné!")
            fini = True
    # TODO : vérifier les autres possibilités de gagnées
    # TODO : vérifier si c'est partie nulle
    # sortir de la boucle si la partie est finie
    if fini:
        break
    # passer à l'autre joueur
    if jeton == "o":
        jeton = "x"
    else:
        jeton = "o"
    # TODO : Défi supplémentaire : faire jouer l'ordinateur (avec ou sans stratégie)