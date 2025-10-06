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

import pytest
import fctListes as moyenne

@pytest.mark.parametrize("j1, j2, resultat_attendu", [
    ("roche", "ciseau", "joueur 1 gagne avec roche."),
    ("roche", "papier", "joueur 2 gagne avec papier."),
    ("Roche", "Papier", "joueur 2 gagne avec Papier.")
])
def test_moyenne(moyenne_rouge, moyenne_vert, moyenne_bleu):
    # Arrange
    resultat_attendu = 3
    # Act
    resultat_division = moyenne(moyenne_rouge, moyenne_vert, moyenne_bleu)

    # Assert
    assert resultat_division == resultat_attendu

# (William qui teste le programme de Sam)

import pytest
from fctListes import pourcentage

def choix_couleur_1_invalide()
    # Arrange
    choix_couleur_1 = hdggj
    # Act
    result = choix_couleur_1_invalide(choix_couleur_1)
    # Assert
    assert not result
def choix_couleur_1_valide()
    # Arrange
    choix_couleur_1 = rouge
    # Act
    result = choix_couleur_1_valide(choix_couleur_1)
    # Assert
    assert not result

def montant_lego_choisi_invalide()
    # Arrange
    montant_lego_choisi = dfghsfg
    # Act
    result = montant_lego_choisi_invalide(montant_lego_choisi)
    # Assert
    assert not result
def montant_lego_choisi_valide()
    # Arrange
    montant_lego_choisi = 5
    # Act
    result = montant_lego_choisi_valide(montant_lego_choisi)
    # Assert
    assert not result