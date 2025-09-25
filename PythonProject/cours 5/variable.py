#variables
texte_1 = "Mon texte" #str string texte
nb_entier_1 = 5     # int integer nombre entier
prix = 5.9555555    # float number nombre décimal
booleen_1 = True    # bool True/False


# affichage
print(texte_1, nb_entier_1, prix, booleen_1)
print("Un nombre", nb_entier_1)
# print(f"...{variable:format}...")   .2f --> décimales
print(f"Prix: {prix: .2f}$") # print(f"...{variable:format}...")   .2f --> décimales

#   entrées
nom = input("Entrer votre nom ") #   input() : récupérer le texte de la console
age = int(input("Entrer votre age "))    # int() : convertir en nombre entier
salaire = float(input("Entrer votre salaire ")) # float() : convertir en nombre décimal

print(nom, age, "ans" )
print(f"Salaire: {salaire:.2f}")