import random

mots = [
    "python", "ordinateur", "programmation", "developpement", "souris", "clavier",
    "ecran", "internet", "reseau", "serveur", "donnees",
    "logiciel", "algorithme", "variable", "fonction", "boucle", "condition",
    "compilation", "debogage", "intelligence", "artificielle", "robot", "cybersecurite"
]

mot_a_trouver = random.choice(mots)
mot_cache = []
for i in range(len(mot_a_trouver)):
    mot_cache.append("_")
lettres_utilisees = []
nb_essais = 6

while "_" in mot_cache and nb_essais > 0:
    print("Mot :", mot_cache)
    print("Lettres utilisées :", lettres_utilisees)
    print("Essais restants :", nb_essais)

    lettre = input("Proposez une lettre ou un mot : ")

    if lettre == mot_a_trouver:
        mot_cache = mot_a_trouver
        trouve = True
        break

    if lettre in lettres_utilisees:
        print("Vous avez déjà utilisé cette lettre.")

    lettres_utilisees.append(lettre)

    trouve = False
    for i in range(len(mot_a_trouver)):
        if list(mot_a_trouver)[i] == lettre:
            mot_cache[i] = lettre
            trouve = True

    if not trouve:
        nb_essais -= 1
        print("Mauvaise lettre !")

if "_" not in mot_cache:
    print("Félicitations, vous avez trouvé le mot ! :", mot_cache)
else:
    print("Dommage, le mot était :", mot_a_trouver)
