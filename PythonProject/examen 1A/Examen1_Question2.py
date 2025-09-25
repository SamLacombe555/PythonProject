# ***********************************************************************
# nombre_chaises_suffisant: Fonction qui déterminer si le nombre de chaises
#                      disponibles est suffisant pour les enfants et les adultes
# ************************** Entrées/sorties ****************************
# Entrées : nb_chaises_adultes, nb_chaises_enfants, nb_enfants, nb_adultes
# Sorties : Aucun
# ***********************************************************************
# Début :
#   	Entrées : nb_chaises_adultes, nb_chaises_enfants, nb_enfants, nb_adultes
#   	Si le nombre d'adultes est supérieur au nombre de chaises disponibles pour les adultes,
#          retourner False.
#   	Calculer le nombre de chaises restantes pour les enfants après avoir assigné les chaises aux adultes.
#   	Si le nombre d'enfants est inférieur ou égal à la somme des chaises disponibles pour les enfants et 
#                                   	des chaises restantes pour les enfants,
#          retourner True.
#   	Sinon,
#          retourner False.
# Fin


# ***********************************************************************
# cout_location_chaises : Fonction qui calcule le coût total de location
#                           des chaises pour les adultes et les enfants.
# ************************** Entrées/sorties ****************************
# Entrées : nb_enfants, nb_adultes
# Sorties : le coût de location des chaises
# ***********************************************************************
# Début :
#   	Entrées : nb_enfants, nb_adultes
#   	Définir les coûts de location par chaise pour un enfant : 5
#   	Définir les coûts de location par chaise pour un adulte : 10
#   	Calculer le coût total pour les enfants : nombre d'enfants * cout chaise enfant
#   	Calculer le coût total pour les adultes : nombre d'adultes * cout chaise adulte
#   	Calculer le coût total global en additionnant les coûts des enfants et des adultes.
#   	Retourner le coût total global.
# Fin


# ***********************************************************************
# Programme principal
# ************************** Entrées/sorties ****************************
# Entrées : nb_enfants, nb_adultes
# Sorties : le coût de location des chaises
# ***********************************************************************
# Début :
#   	Lire le nombre de chaises adulte
#   	Lire le nombre de chaises enfant
#   	Lire le nombre d'adultes
#   	Lire le nombre d'enfants
#
#       Appeler la fonction nombre_chaises_suffisant pour savoir si le nombre de chaises est suffisant.
#       Si le nombre de chaises est suffisant
#           retourne True.
#       Si la fonction retourne True :
#           Afficher "Le nombre de places est suffisant."
#           Calculer le coût total de location en appelant la fonction cout_location_chaises.
#           Afficher le coût total de location.
#       Sinon :
#           Afficher "Le nombre de places est insuffisant"
# Fin
