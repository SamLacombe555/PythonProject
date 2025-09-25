#####################################################################

# Associer les commentaiers aux bons blocs de conditions :

#####################################################################











#####################################################################
# Comparaison de chaînes de caractères

mot_de_passe = "abc123"
confirmation = "abc123"
if mot_de_passe == confirmation:
    print("Mot de passe confirmé")
else:
    print("Les mots de passe ne correspondent pas")

#####################################################################
# Utilisation de and pour vérifier deux conditions en même temps

temperature = 30
vent = 5
if temperature > 25 and vent < 10:
    print("Il fait chaud et il y a peu de vent")

######################################################################
# Comparer des variables avec and et or

age = 22
diplome = "baccalauréat"
if age >= 18 and diplome == "baccalauréat":
    print("Vous êtes éligible à l'université")

#######################################################################
# Utilisation de or pour vérifier si au moins une condition est vraie

jour = "samedi"
meteo = "pluie"
if jour == "samedi" or jour == "dimanche":
    print("C'est la fin de semaine")

########################################################################
# Déterminer un résultat basé sur des niveaux de conditions

annees_de_pratique = 3
if annees_de_pratique >= 10:
    print("Expert")
elif annees_de_pratique >= 5:
    print("Intermédiaire")
elif annees_de_pratique >= 1:
    print("Débutant")
else:
    print("Novice")

########################################################################
# Utiliser != et combiner plusieurs conditions

role = "utilisateur"
age = 20
if role != "admin" and age >= 18:
    print("Accès limité autorisé.")
else:
    print("Accès complet ou interdit.")

#####################################################################
# Comparer deux variables et utiliser not pour vérifier l'inverse d'une condition

nombre = 50
if nombre > 0 and not nombre == 100:
    print("Le nombre est positif et différent de 100.")
else:
    print("Le nombre est négatif, zéro, ou égal à 100.")

########################################################################
# Vérifier si une valeur est en dehors d'une plage

temperature = 30
if temperature < 15 or temperature > 25:
    print("Température inconfortable.")
else:
    print("Température confortable.")

########################################################################