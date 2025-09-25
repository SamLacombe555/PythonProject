def explorer_lieu(lieu):
    """
    Affiche un message indiquant que le joueur explore un lieu donné.
    :param lieu: Le nom du lieu à explorer.
    :return:
    """
    print(f"Vous explorez {lieu}...")

def ramasser_objet(objet, sac):
    """
    Ajoute un objet au sac.
    :param objet: L'objet à ramasser (sous forme de texte)
    :param sac: Chaîne de caractères contenant tous les objets
    :return: Le contenu du sac après l'ajout de l'objet.
    """
    sac = sac + f"[{objet}] "
    return sac

def verifier_objet(objet, sac):
    """
    Vérifie si un objet se trouve déjà dans le sac (chaîne de caractères).
    :param objet: L'objet à trouver.
    :param sac: Le sac dans lequel chercher.
    :return: True ou False selon si l'objet de trouve dans le sac ou non.
    """
    return objet in sac

def calculer_points(sac):
    """
    Calcule un score basé sur le nombre d’objets collectés.
    Chaque objet vaut 10 points.
    :param sac: Le sac dans lequel chercher
    :return: Un entier représentant le score.
    """
    if sac.strip() == "":
        return 0

    # Calcule la quantité d'objets dans la chaîne de caractères.
    objets = sac.strip().split(" ")
    return len(objets) * 10

def mission_aventure(nom_joueur, sac):
    """
    - Lance une mini-mission pour un joueur :
    - Explore un lieu
    - Ramasse une clé magique
    - Vérifie si la clé est bien dans le sac
    :param nom_joueur: Le nom du joueur.
    :param sac:
    :return: Le sac mis à jour
    """

    explorer_lieu("la forêt enchantée")
    sac = ramasser_objet("clé_magique", sac)
    objet_dans_sac = verifier_objet("clé_magique", sac)

    if objet_dans_sac == True :
        print(f"{nom_joueur} a trouvé la clé !")

    return sac

if __name__ == "__main__":
    joueur = "Alice"
    inventaire = ""

    inventaire = mission_aventure(joueur, inventaire)

    objet_dans_sac = verifier_objet("clé_magique", inventaire)

    if objet_dans_sac == True:
        print("La porte peut être ouverte !")
    else:
        print("Il manque quelque chose...")

    # Calcul de score à partir du sac
    score = calculer_points(inventaire)
    print(f"Score final de {joueur} : {score} points")

"""
1. ramasser_objet, verifier_objet, mission_aventure
2. ramasser_objet, verifier_objet, calculer_points, mission_aventure
3. mission_aventure
4. 
5. lieu, objet, sac, nom_joueur, 
6. 
7. 
8.
9.objet dans sac, score
10.
"""