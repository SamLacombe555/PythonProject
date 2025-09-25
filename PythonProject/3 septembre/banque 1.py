solde = 1000
print("Bienvenu à la Banque !")
print("-" * 30)

def menu_banque():
    print("1 - Afficher solde")
    print("2 - Dépot")
    print("3 - Retrait")
    print("4 - Quitter")

def afficher_solde():
    print(f"{"Solde":<20} : {solde:>20}")

def deposer(montant, solde):
    """

    :param montant: montant du dépôt
    :param solde: solde initiale
    :return: le solde
    """

    solde = solde + montant
    return solde

def retirer(montant, solde):
    """

    :param montant: montant du retrait
    :param solde: solde initiale
    :return: le nouveau soldesolde
    """

    solde = solde - montant
    return solde

print("Veuillez vous connecter")
while True: # répéter la connexion
    no = input("No de carte: ")
    nip = input("NIP: ")
    if nip == "1234": # valider le nip
        break # terminer la boucle
    else:
        print("Erreur, essayez de nouveau")

while True:
    menu_banque()
    choix = input()

    if choix == "1":
        afficher_solde()
    elif choix == "2":
        depot = int(input("Dépôt: "))
        solde = deposer(depot, solde)
        afficher_solde()
    elif choix == "3":
        retrait = int(input("Retrait: "))
        solde = retirer(retrait, solde)
        afficher_solde()
    elif choix == "4":
        print("Merci d'avoir utilisé notre service bancaire. Au revoir !")
        break # terminer boucle
    else:
        print("Choix invalide, veuillez réessayer.")

