def verifier(valeur, seuil_inf, seuil_sup):
    """
    Fonction pour vérifier automatiquement si des valeurs spécifiques
    :param valeur: valeur : à vérifier
    :param seuil_inf: seuil inférieur de la plage
    :param seuil_sup:seuil  supérieur de la plage
    :return: vrai si la valeur est dans la plage
    """

    if valeur < seuil_inf:
        return False
    elif valeur > seuil_sup:
        return False
    else:
        return True

"""
    return valeur >= seuil_inf and valeur <= seuil_sup
"""

print(verifier(134.73, 120, 139))
assert verifier(228.67, 137.62, 228.65) == False
assert verifier(74.22, 71.13, 77.16 ) == True

