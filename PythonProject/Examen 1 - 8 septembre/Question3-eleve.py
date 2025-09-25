"""
A) Variables
    Nombre de livres lus / entrée / integer
    Abonnement premium / entrée / booléen - string
    Livre rare emprunté au dessus de deux semaines / entrée / booleen - string
"""

#B) Pseudocode

#print Bienvenue!
#demande nbr de livres lus
#demande si abonnement est premium
#demande si ceci serait la 2e semaine d'affilée avec livre rare


#si nbr de livres lus >= 10
    #True = print accepté
    #false = print refusé

#si nbr de livres lus >= 5 et que abonnement est premium
    #true = print accepté
    #false = print refusé

#si ceci serait la 2e semaine d'affilée avec livre rare
    #true = print refusé
    #false = print accepté



def verification(livres, abonnement, semaines):
    """
    Fonction qui détermine si le membre est légible pour emprunter un livre rare
    :param livres: Nombre de livres lus
    :param abonnement: Possède un abonnement premium
    :param semaines: Ceci serait la 2e semaines d'affiler qu'il emprunter un livre rare
    :return: Aucun
    """

    if (livres >= 10 or (livres >=5 and abonnement == "oui")) and semaines != "oui":
        print("Votre demande est acceptée!")
    else:
        print("Votre demande est refusée")

#Bienvenue
print("Bienvenue au club de lecture!")
print("Pour emprunter un livre rare, svp répondez à ces prochaines questions:")


#Questionne le membre qui veut emprunter un livre rare
nombre_livres = int(input("Combien de livres avez-vous lus?"))
type_abonnement = str(input("Possédez-vous l'abonnement premium?"))
montant_semaines = str(input("Ceci est-il la 2e semaine d'affilée que vous emprunterez un livre rare?"))

#Vérifie sa demande
verification(nombre_livres,type_abonnement,montant_semaines)
