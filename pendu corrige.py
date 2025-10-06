import random

#----------------------------------------JP----------------------------------------
def trouver_et_remplacer(le_mot: str | list[str], lettres_decouvertes: list[str], lettre_devinee: str) -> bool:
    """
    Insère la lettre devinée dans la liste de lettres visibles si elle est dans le mot.
    Retourne True si une nouvelle lettre a été trouvée, False sinon.
    """
    trouve: bool = False
    for index, lettre_du_mot in enumerate(le_mot):
        if lettre_du_mot == lettre_devinee and (lettres_decouvertes[index] != lettre_du_mot):
            lettres_decouvertes[index] = lettre_du_mot
            trouve = True
    return trouve


#----------------------------------------Jess : ASCII art----------------------------------------
PENDU_ASCII = [
    """
       .________.
       |        |
       |
       |
       |
       |
    ___|___
    """,
    """
       .________.
       |        |
       |        O
       |
       |
       |
    ___|___
    """,
    """
       .________.
       |        |
       |        O
       |        |
       |
       |
    ___|___
    """,
    """
       .________.
       |        |
       |        O
       |       /|
       |
       |
    ___|___
    """,
    """
       .________.
       |        |
       |        O
       |       /|\\
       |
       |
    ___|___
    """,
    """
       .________.
       |        |
       |        O
       |       /|\\
       |       /
       |
    ___|___
    """,
    """
       .________.
       |        |
       |        O
       |       /|\\
       |       / \\
       |
    ___|___
    """
]


#----------------------------------------Mode principal (JD + SL + FA)----------------------------------------
def jouer_pendu():
    # Banque de mots (ajout idée de William : plus de variété)
    liste_mots = ["jouer", "python", "coqueluche", "boucle", "codage", "javascript", "exercice"]

    motchoisi = random.choice(liste_mots).lower()

    liste_lettres_visible: list[str] = ['_' for _ in motchoisi]
    liste_lettres_utilisees: list[str] = []

    # Idée de William : nombre d'essais = longueur du mot + 2 (au lieu de fixe)
    nombre_essai: int = len(motchoisi) + 2

    while True:
        print(PENDU_ASCII[min(len(PENDU_ASCII)-1, (len(motchoisi)+2) - nombre_essai)])  # affiche ASCII
        print(f"\nMot : {' '.join(liste_lettres_visible)}")
        print(f"Lettres devinées : {', '.join(liste_lettres_utilisees)}")
        print(f"Il te reste {nombre_essai} essais!")

        lettre = input("Devine une lettre: ").lower()

        if not lettre.isalpha() or len(lettre) != 1:
            print("Veuillez entrer une seule lettre valide.")
            continue

        if lettre in liste_lettres_utilisees:
            nombre_essai -= 1
            print("La lettre a déjà été utilisée. Vous perdez une vie!")
            continue

        liste_lettres_utilisees.append(lettre)

        if lettre not in motchoisi:
            nombre_essai -= 1
            print("La lettre n'est pas dans le mot. Vous perdez une vie!")
        else:
            print("Bonne réponse!")
            trouver_et_remplacer(motchoisi, liste_lettres_visible, lettre)

        if nombre_essai <= 0:
            print(PENDU_ASCII[-1])
            print("\nVous avez perdu. Dommage!")
            print(f"Le mot était : {motchoisi}")
            break
        elif "".join(liste_lettres_visible) == motchoisi:
            print("\nFélicitations, vous avez gagné!")
            print(f"Le mot était : {motchoisi}")
            break


#----------------------------------------Extension Julien Legault / Sow.L----------------------------------------
def choisir_mode():
    print("=== Jeu du Pendu ===")
    print("1. Mode classique (mot aléatoire)")
    print("2. Mode 2 joueurs (un joueur entre un mot)")
    choix = input("Choisissez un mode (1/2): ")

    if choix == "2":
        while True:
            mot = input("Joueur 1, entrez un mot secret: ").lower()
            if len(mot) < 3:
                print("Le mot doit contenir au moins 3 lettres.")
                continue
            if not mot.isalpha():
                print("Le mot doit contenir uniquement des lettres.")
                continue
            return mot
    else:
        return random.choice(["jouer", "python", "coqueluche", "boucle", "codage", "javascript", "exercice"]).lower()


#----------------------------------------Lancement----------------------------------------
if __name__ == "__main__":
    jouer_pendu()
