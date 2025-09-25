"""
La température ne doit pas descendre sous 18 °C et ne doit pas dépasser 27 °C.

L’humidité doit se situer strictement entre 30 % et 50 %.

La poussière est acceptable seulement si elle est faible."""
def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : humidité

    Retour :
    - "Tout est sous contrôle!" si tout est bon
    - "Environnement non optimal" les problèmes sinon
    """
    alerte = False

    if temp < 18:
        message_temp = "Température trop basse"
        alerte = True
    elif temp > 27:
        message_temp = "Température trop élevée"
        alerte = True
    else:
        message_temp = "Température est bonne"

    if poussiere == "faible":
        message_poussiere = "Pas assez de poussière"
    else:
        message_poussiere = "Trop de poussière"
        alerte = True

    if humidite <= 30:
        message_humidite = "Humidité trop basse"
        alerte = True
    elif humidite >=50:
        message_humidite = "Humidité trop élevée"
        alerte = True
    else:
        message_humidite = "Humidité est bonne"


    print(message_temp)
    print(message_poussiere)
    print(message_humidite)

    if alerte:
        return "Environnement non optimal"
    else:
        return "Tout est sous contrôle!"

if __name__ == "__main__":
    print(environnement_optimal(25, "faible", 40))
