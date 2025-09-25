# 3 niveau min + 1000 pièce d'or min + 500 unité bois min
#   climat normal

niveau = (int(input("Il y a combien de niveau du château?")) >= 3)
d_or = (int(input("Il y a combien de pièce d'or?")) >= 1000)
bois = (int(input("Il y a combien d'unité de bois?")) >= 500)
climat = bool(int(input("Est-ce que le climat est normal?")))

if (niveau and d_or and bois) or climat == True:
    print("Le joueur peut construire une nouvelle tour dans son château")
else:
    print("Le joueur ne peut pas construire une nouvelle tour dans son château")

