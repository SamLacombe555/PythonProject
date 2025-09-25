piece = int(input("Combien de pièces avez-vous?"))
cle = bool(input("Avez-vous trouvez la clé secrète?"))
vip = bool(input("Possédez-vous la passe VIP?"))


if piece > 50 and cle == True:
    print("Accepté")
elif vip == True:
    print("Accepté")
else:
    print("Refusé")
