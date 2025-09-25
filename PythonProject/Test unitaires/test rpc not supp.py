def roche_papier_ciseau(choix_joueur1:str, choix_joueur2:str) -> None:
    """
    Cette fonction compare les choix du jeu Roche-Papier-Ciseaux entre deux
    joueurs et affiche le gagnant.

    :param choix_joueur1: Le choix du joueur 1 ("roche", "papier" ou "ciseau")
    :param choix_joueur2: Le choix du joueur 2 ("roche", "papier" ou "ciseau")
    :return: Aucun
    """
    armes = ["roche", "papier", "ciseau"]

    if choix_joueur1 not in armes or choix_joueur2 not in armes:
        print("Vous n'avez pas entré roche, papier ou ciseau. :(")
    else:
        if choix_joueur1 == choix_joueur2:
            print("Partie nulle!")
        elif (choix_joueur1 == 'roche' and choix_joueur2 == 'ciseau') or (choix_joueur1 == 'ciseau' and choix_joueur2 == 'papier') or (choix_joueur1 == 'papier' and choix_joueur2 == 'roche'):
            joueur_gagnant = "joueur1"
            arme_gagnante = choix_joueur1
        elif (choix_joueur1 == 'roche' and choix_joueur2 == 'papier') or (choix_joueur1 == 'ciseau' and choix_joueur2 == 'roche') or (choix_joueur1 == 'papier' and choix_joueur2 == 'ciseau'):
            joueur_gagnant = "joueur2"
            arme_gagnante = choix_joueur2

        print(f"\nLe gagnant est {joueur_gagnant} avec {arme_gagnante}, félicitation.")

if __name__ == "__main__":

    print("""
    Bienvenu au jeu Roche-Papier-Ciseau.
    Veuillez faire un choix parmi les suivants : 
    roche
    papier
    ciseau
     """)

    choix1 = str(input("Choix du joueur 1 : "))
    choix2 = str(input("Choix du joueur 2 : "))

    roche_papier_ciseau(choix1, choix2)
