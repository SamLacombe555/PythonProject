def calcul_pv(joueur_pv: int, joueur_def: int, attack: int) -> str:
    """

    :param joueur_pv: C'est les PVs du joueur défendant
    :param joueur_def: C'est la Déffence du joueur défendant
    :param attack: C'est l'attaque du joueur attaquant
    :return: Retourne un str qui dit combien le défendant a pris de domages et combien il lui reste de pv
    """
    attack -= joueur_def
    joueur_pv -= attack
    return f"Le joueur defendant a pris {attack} points de dommage, et lui reste {joueur_pv} points de vie!"