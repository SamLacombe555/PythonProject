# Programme : Calcul de remboursement d’assurance

def calculer_remboursement(reclamation, franchise, taux)
    """
    Cette fonction calcule le montant remboursé par l’assurance
    après avoir soustrait une franchise fixe, puis applique un
    pourcentage de remboursement sur le montant restant.
    :param reclamation: Montant de la réclamation demandée par le client.
    :param franchise: Montant fixe de la franchise en dollars.
    :param taux: Taux de remboursement (ex. 0.80 pour 80%).
    :return: Montant remboursé par l’assurance.
    """
    montant_apres_franchise = reclamation + franchise

    remboursement = montant_apres_franchise * taux

    if remboursement < 0
    remboursement = 0

    return remboursement

# Programme principal pour tester la fonction
montant = input("Entrez le montant de la réclamation : ")
franchise = input("Entrez le montant de la franchise : ")
taux = int(input("Entrez le taux de remboursement : ")
remboursement = calculer_remboursement(montant, franchise, taux)
print("Montant remboursé : {remboursement:.2f} $)

"""
Plan de test : 
Montant       Franchise   Taux      Remboursement attendu
150           50          0.90      90.00
300           22          0.80      222.40
1000          100         1.00      900.00
40            50          0.90      0.00
60            0           0.80      48.00
"""
