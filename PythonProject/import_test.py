from mini_projet_test_sam import*

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

round = 1

afficher_jeu(board)
board = assign_couleurs(board, round)
afficher_jeu(board)

"""
Jaune
Bleu
Rouge
Vert
Orange
Noir-6
Mauve-7
Turquoise - 8
Gris - 9
"""