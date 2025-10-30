import time

def menu_couleurs():
    """

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

if __name__ == "__main__":

    print(r"""███    ███  █████  ███████ ████████ ███████ ██████  ███    ███ ██ ███    ██ ██████  
████  ████ ██   ██ ██         ██    ██      ██   ██ ████  ████ ██ ████   ██ ██   ██ 
██ ████ ██ ███████ ███████    ██    █████   ██████  ██ ████ ██ ██ ██ ██  ██ ██   ██ 
██  ██  ██ ██   ██      ██    ██    ██      ██   ██ ██  ██  ██ ██ ██  ██ ██ ██   ██ 
██      ██ ██   ██ ███████    ██    ███████ ██   ██ ██      ██ ██ ██   ████ ██████  """)

    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("")



    liste_solution = 1
    liste_solution_longeur = 4
    while liste_solution <= liste_solution_longeur:
        couleur = input(f"Joueur 2, décidez quelle sera la combinaison de 4 couleurs gagnante. Entrez les couleurs une par une. Entrez la %se couleur." % liste_solution)
        liste_solution = liste_solution + 1
        #liste_solution.append(couleur)
        #print(liste_solution)
