import pytest
import MASTERMIND_fonctions *

@pytest.mark.parametrize

def test_noms():
    """
    Cette fonction compare le nom que l'utilisateur a entré et le nom affiché dans nom_codificateur.
    :return:
    """
    assert



def test_couleurs_solution():
    """
    Cette fonction vérifie si liste_solution a 4 couleurs différentes ou non.
    :return:
    """
    assert



def test_pions():
    """
    Cette fonction teste si le nombre de pions rouges et blancs est exact.
    :return:
    """
    assert



@pytest.mark.parametrize("mots, longueur", [
    (["banane", "orange", "pomme"], 3),
    (["banane", "orange", "pomme", "sadlhaosd", "aksdas"], 5),
    (["banane", "orange"], 2),
    ([], 0)
])
def test_hasher_mots(mots, longueur):

    dict_hash = crypt.hasher_mots(mots)

    assert isinstance(dict_hash, dict)
    assert len(dict_hash) == longueur
    if len(dict_hash) != 0:
        assert len(dict_hash[mots[0]]) == 3


@pytest.mark.parametrize("initial, nb_cesar, chaine_attendue",[
    ("abcde", 2, "cdefg"),
    ("abcde", 0, "abcde"),
    ("abcde", 10, "klmno"),
    ("abcde", 26, "abcde"),
    ("cdefg", -2, "abcde"),
    ("zoo", 3, "crr")
])
def test_chiffrement_cesar(initial, nb_cesar, chaine_attendue):

    chaine_cesar = crypt.chiffrement_cesar(initial, nb_cesar)

    assert isinstance(chaine_cesar, str)
    assert len(chaine_cesar) == len(initial)
    assert chaine_cesar == chaine_attendue







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