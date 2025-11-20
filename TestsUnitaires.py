from pytest import *
from MASTERMIND_fonctions import *

round = 1
liste_solution = ["_", "_", "_", "_"]
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

liste_couleurs_random = ['J', 'B', 'R', 'V', 'O', 'N', 'M', 'T', 'G']


def test_noms():#will
    """
    Cette fonction compare le nom que l'utilisateur a entré et le nom affiché dans nom_codificateur.
    :return:
    """
    nom_codificateur = "Sam"
    str_input_joueur = "Sam"
    assert nom_codificateur == str_input_joueur

def test_couleurs_solution():#will
    """
    Cette fonction prévient d'avoir 2 couleurs pareilles dans la liste solution.
    :return:
    """
    liste_solution = ['J', 'B', 'R', '_']
    choix_c = "R"
    if choix_c in liste_solution:
        print("La solution ne peut pas contenir deux fois la même couleur.")
        deux_couleurs = True
    resultat = deux_couleurs
    assert resultat == True



def test_pions():#will/sam
    """
    Cette fonction teste si le nombre de pions rouges et blancs est exact.
    :return:
    """
    liste_solution = ['J', 'B', 'R', 'V']
    board = [

    ["J", "B", "V", "R"],
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
    round = 1
    resultat = j2_verifie(board,liste_solution,round)
    assert resultat == [

    ["J", "B", "V", "R", "2 rouge(s), 2 blanc(s)"],
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

def test_win_condition():#will
    """
    Cette fonction vérifie si la partie a été gagné par le joueur décodeur.
    :return:
    """
    liste_solution = ['J', 'B', 'R', 'V']
    round = 12
    board = [

    ['J', 'R', 'V', 'O', '1 rouge(s), 2 blanc(s)'],
    ['G', 'T', 'M', 'N', '0 rouge(s), 0 blanc(s)'],
    ['T', 'M', 'N', 'O', '0 rouge(s), 0 blanc(s)'],
    ['M', 'N', 'O', 'V', '1 rouge(s), 0 blanc(s)'],
    ['N', 'O', 'V', 'R', '0 rouge(s), 2 blanc(s)'],
    ['O', 'V', 'R', 'B', '1 rouge(s), 2 blanc(s)'],
    ['V', 'R', 'B', 'J', '0 rouge(s), 4 blanc(s)'],
    ['R', 'B', 'J', 'G', '1 rouge(s), 2 blanc(s)'],
    ['B', 'J', 'G', 'T', '0 rouge(s), 2 blanc(s)'],
    ['J', 'G', 'T', 'M', '1 rouge(s), 0 blanc(s)'],
    ['O', 'N', 'M', 'T', '0 rouge(s), 0 blanc(s)'],
    ['J', 'B', 'R', 'V']

    ]
    resultat = verifier_fin(board, liste_solution, round)
    assert resultat == 1