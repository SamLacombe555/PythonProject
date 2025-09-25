import pytest # importe le module pytest pour faire des tests unitaires
from ExDebug1 import environnement_optimal # lien avec la fonction de notre autre fichier

# Test unitaire pour la fonction environnement_optimal
def test_environnement_optimal():
    # Arrange : préparer les valeurs des variables d'entrées et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    # Act: appeler la fonction
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu


# Test unitaire pour la fonction environnement_optimal
def test_environnement_optimal_2():
    # Arrange : préparer les valeurs des variables d'entrées et le résultat attendu
    temperature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    # Act: appeler la fonction
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu


# Test unitaire pour la fonction environnement_optimal
def test_environnement_optimal_3():
    # Arrange : préparer les valeurs des variables d'entrées et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 20
    resultat_attendu = "Environnement non optimal"

    # Act: appeler la fonction
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu


# Test unitaire pour la fonction environnement_optimal
def test_environnement_optimal_4():
    # Arrange : préparer les valeurs des variables d'entrées et le résultat attendu
    temperature = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environnement non optimal"

    # Act: appeler la fonction
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # Assert : vérifier si le résultat obtenu correspond au résultat attendu
    assert resultat_attendu == resultat_obtenu

