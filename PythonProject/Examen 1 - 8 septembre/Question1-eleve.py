# Programme : Calcul de remboursement d’assurance

def calculer_remboursement(reclamation, franchise, taux):   #Il manquait un ":" à la fin de la ligne
    """
    Cette fonction calcule le montant remboursé par l’assurance
    après avoir soustrait une franchise fixe, puis applique un
    pourcentage de remboursement sur le montant restant.
    :param reclamation: Montant de la réclamation demandée par le client.
    :param franchise: Montant fixe de la franchise en dollars.
    :param taux: Taux de remboursement (ex. 0.80 pour 80%).
    :return: Montant remboursé par l’assurance.
    """
    montant_apres_franchise = reclamation - franchise   #La franchise doit soustraire sa valeur sur la réclamation et non s'additionner

    remboursement = montant_apres_franchise * taux

    if remboursement < 0:   #Il manquait un ":" a la fin de la ligne
        remboursement = 0

    return remboursement

# Programme principal pour tester la fonction
montant = int(input("Entrez le montant de la réclamation : "))  #On doit spécifier que le input est un integer
franchise = int(input("Entrez le montant de la franchise : "))  #On doit spécifier que le input est un integer
taux = float(input("Entrez le taux de remboursement : "))   #Ce input n'est pas devrait pas être un integer, mais plutôt un float car on accepte ses valeurs avec des décimales. De plus, il manquait un ")" à la fin de la ligne
remboursement = calculer_remboursement(montant, franchise, taux)
print(f"Montant remboursé : {remboursement:.2f} $") #Il manquait un '"' entre le "$" et le ")"

"""
Plan de test : 
Montant       Franchise   Taux      Remboursement attendu
150           50          0.90      90.00
300           22          0.80      222.40
1000          100         1.00      900.00
40            50          0.90      0.00
60            0           0.80      48.00
"""
