paye1 = int(input("Est-ce que le client a payé en ligne? \nTaper 1 pour Oui ou 0 pour Non"))

if paye1 == 0 :
    paye2 = int(input("Est-ce veux payer à la livraison? \nTaper 1 pour Oui ou 0 pour Non"))

meteo = int(input("Est-il orageux? \nTaper 1 pour Oui ou 0 pour Non"))
if meteo == 1 :
    vehicule = int(input("ESt-ce que le livreur a un véhicule protégé? \nTaper 1 pour Oui ou 0 pour Non"))


if (paye2 == 0 and vehicule == 0):
    print("Commande non valide pour livraison")
else:
    print("Commande valide pour livraison")
    
