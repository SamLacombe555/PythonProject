# fonction qui ajout les bonbons dans le sac
def mettre_dans_sac(bonbons, sac):
    """
    Fonction pour mettre les bobons dans le sac
    :param bonbons: nb de bonbons
    :param sac: le nb de bonbons déjà dans le sac
    :return: le nouveau total de bonbons dans le sac
    """
    sac += bonbons
    return sac

# programme principal : ramasser des bonbons à l'halloween
limite = int(input("Ton sac peut contenir combien de bonbons?"))
sac = 0
while sac < limite:
    nb_bonbons = int(input("Combien de bonbons tu as rammassé?"))
    sac = mettre_dans_sac(nb_bonbons, sac)

print("Total de bonbons dans le sac: ", sac)








