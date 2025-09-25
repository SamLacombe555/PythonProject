"""
solde = 1000
retrait = int(input("Retrait : "))

if retrait <= solde and retrait > 0:
    solde = solde - retrait
    print("Nouveau solde: ", solde)
else:
    print("Erreur")
"""


"""
solde = 1000
retrait = int(input("Retrait : "))
# conditions de retrait non valide
if retrait > solde or retrait <= 0:
    print("Erreur")
else:
    solde = solde - retrait
    print("Nouveau solde: ", solde)
"""



solde = 1000

while True: # boucle pour redemander le montant jusqu'à ce qui'il soit valide
    retrait = int(input("Retrait : "))
    # conditions de retrait non valide
    if retrait > solde:
        print("Erreur: solde insufisant")
    elif retrait <= 0:
        print("Erreur: le nombre doit être positif")
    else: # retrait valide
        break # terminer la boucle
# poursuivre le programme
solde = solde - retrait
print("Nouveau solde: ", solde)




