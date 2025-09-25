import random

# ----------------------------------------Vann Sovannthanant ✅----------------------------------------

# I have absolutly no idea of what I am doing. """"""
print("-" * 20)
"""
def essaie(mots_cacher, tentative, chance):

    Fonction qui détermine si la lettre entrer est bonne ou mauvais. ✅❌
    :return: Enlève une chance si la lettre est mauvais.

    while True:
        tentative = str.upper(input("Entrez une lettre"))
        if tentative == "P":
            mots_cacher = "P_____"
            return tentative
            print(tentative)
        elif tentative == "Y":
            mots_cacher = "_Y____"
            return tentative
            print(tentative)
        elif tentative == "T":
            mots_cacher = "__T___"
            return tentative
            print(tentative)
        elif tentative == "H":
            mots_cacher = "___H__"
            return tentative
            print(tentative)
        elif tentative == "O":
            mots_cacher = "____O_"
            return tentative
            print(tentative)
        elif tentative == "N":
            mots_cacher = "_____N"
            return tentative
            print(tentative)
        else:
            chance = chance - 1
            return chance
            print(chance)

        """

mots_cacher = ["_______"]  # Mettre _ * len(motchoisi) - JD
mots_reveler = ["PYTHON"]  # Mettre la variable motchoisi comme valeur à mots_reveler - JD
chance = 5


# essaie()
# reponse()


def trouver_et_remplacer(le_mot: str | list[str], lettres_decouvertes: list[str], lettre_devinee: str) -> bool:  # JP
    """
    Insère la lettre devinée dans la liste de lettres à découvrir si elle est dans le mot et elle n'a pas déja été découverte.
    :param le_mot: Le mot à deviner (soit un string, soit une liste des lettres du mot).
    :param lettres_decouvertes: La liste de lettres à découvrir.
    :param lettre_devinee: La lettre qui a été devinée.
    :return: Vrai une *nouvelle* lettre a été découverte, sinon Faux.
    """
    trouve: bool = False
    for index, lettre_du_mot in enumerate(le_mot):
        if lettre_du_mot == lettre_devinee and (lettres_decouvertes[index] != lettre_du_mot):
            lettres_decouvertes[index] = lettre_du_mot
            trouve = True
    return trouve


# Programme principal-----------------------------------------------
# Maryse

# Créer une liste de mots #ls
liste_mots = ["jouer", "python", "coqueluche", "boucle"]

# Choisir un mot au hasard JD
lListe = len(liste_mots)  # Je viens chercher la longueur de la liste - Jonathan
randomMot = random.randint(0,
                           lListe)  # Je vais chercher un nombre au hasard entre 0 et la longueur de la liste de mots - Jonathan
motchoisi = liste_mots[randomMot]  # Je viens chercher mot à l'indice du nombre aléatoire - Jonathan
len_liste = len(motchoisi)  # La longueur du mot choisi
liste_char_cherche = []  # Liste des charactères du mot choisi
i = 0  # Indice de la liste pour les charactères de la liste du mot choisi
# Il faudrait probablement changer les noms des variables pour respecter les conventions - JP
while i <= len_liste:
    liste_char_cherche.append(motchoisi[i])
    i += 1

# Créer la liste de lettres du mot caché (JP)
liste_lettres_visible: list[str] = ['_' for _ in motchoisi]

# Créer la liste de lettres utilisées
liste_lettres_utilisees: list[str] = []  # (FA)

# Définir le nombre de vies restantes (JP)
nombre_essai: int = 5

while True:
    # Afficher le mot caché, les lettre utilisées et le nombre d'essais (SL)
    print(f"Mot : {liste_lettres_visible}")  # Liste des lettres trouvés en ordre du mots
    print(f"Lettres devinées : {liste_lettres_utilisees}")  # Listes des lettres utilisées
    print(f"Il te reste {nombre_essai} essais!")  # nombre d'essais restant

    lettre = input("Devine une lettre: ")  # demander une lettre (FA)
    # vérifier si la lettre est dans le mot et l'ajouter aux lettres utilisées (JP)
    if lettre in liste_lettres_utilisees:
        nombre_essai -= 1
        print("La lettre a déjà été utilisée. Vous perdez une vie!")
    elif lettre not in motchoisi:
        nombre_essai -= 1
        liste_lettres_utilisees.append(lettre)
        print("La lettre n'est pas dans le mot. Vous perdez une vie!")
    else:
        liste_lettres_utilisees.append(lettre)
        print("Vous avez deviné correctement!")
        trouver_et_remplacer(motchoisi, liste_lettres_visible, lettre)  # Noter que liste_lettres_visible est mutable

    # vérifier si on a gagné ou perdu (JP)
    if nombre_essai <= 0:
        print("Vous avez perdu. Dommage!")
        print(f"Le mot était : {motchoisi}")
        break
    elif "".join(liste_lettres_visible) == motchoisi:
        print("Vous avez gagné!")
        print(f"Le mot était : {motchoisi}")

# Maryse, je peut décorer les réponses? Répondre ici:

# Junior
# Il faut une banque de mots
# ["mot1", "mot2", "mot3", ...]
# Choisir un mot au hasard de la banque de mots
# Créer deux listes : les lettres du mot et la liste de lettres à découvrir initialisée avec autant d'espaces vides ("_") qu'il y a de lettres.
# Créer une listes pour les lettres qui ont déjà été devinées
# Définir le nombre de vies
# Jusqu'à la fin du jeu:
#   Afficher la liste de lettres à découvrir
#   Définir et afficher le nombre de vies
#   Demander à l'utilisateur d'entrer une lettre (et valider l'input)
#   Si la lettre a déjà été devinée:
#      L'utilisateur perd une vie
#   Sinon, si la lettre n'est pas dans le mot:
#      L'utilisateur perd une vie
#      La lettre est ajoutée à la liste des lettres devinées
#   Sinon:
#       Ajouter la lettre à la liste de lettres devinées
#       ---trouver_et_remplacer---
#       Pour chaque paire d'indice et de lettre dans le mot:
#           Si la lettre correspond à la lettre devinée:
#               Dans la liste de lettres à découvrir, à l'indice actuel, remplacer cet élément par la lettre devinée.
#       ---trouver_et_remplacer---
#   Si la liste de lettres à découvrir est remplie ("".join(lettres_decouvertes) == mot):
#       Afficher un message de gagne et briser la boucle
#   Sinon, l'utilisateur n'a plus de vie:
#       Afficher un message de perte et briser la boucle

# G
"""
liste de mots [mots 1, mots2, mots3,]
donner a l'utilisateur 3 essaie
demander a l'utilisateur de rentrer une lettre
si lettre est correcte l'utilisateur ne perd pas d'essaie
sinon perd 1 essaie et le jeu continue
si plus d'essaie = jeu fini
si trouver le mots = jeu fini
liste qui recois le mots,
liste qui cache les mots

"""

# ------------------------------------------------------------------------
# Mille sabords
# William

# Choisir un mot au hasard
# liste_mots = [python, codage, javascript]
# mot = random.choice(liste_mots)
# lettres_trouves = []
# tours_restants = len(mot) + 2
# mot_a_trouver = ['_'] * len(mot)

# print("Essayez de deviner une lettre du mot caché.")

# while tours_restants > 0 et '_' in mot_a_trouver

# ------------------------------------------------------------------------

# Julien Legault
"""
Besoin d'input (str) qui demande un mot caché
liste qui prend le mot 
liste qui cache le mot caché
Un nombre d'essai maximum
Demande une lettre (si déjà prise refaire la sélection de lettre)

Fonction choisir_mot 
While True:    
    mot = input("Veuillez choisir un mot de 7 lettres : ")
    if len(mot) != 7:
        #vérifier la longueur du mot
        print("Le mot doit contenir 7 lettres.")
        continue 
    if not mot.isalpha():
        print("Le mot doit contenir uniquement des lettres. ")
        continue
#(programme principal)choisir_mot = mot_choisi
Fonction lettre_choisi

liste de lettre à choisir [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
liste vide avant le mot choisi [ , , , , , , ]

"""
# Samuel Lacombe (SL)
""""
le mot est "exercice"
liste cachée est [e,x,e,r,c,i,c,e]
liste visible est [#,#,#,#,#,#,#,#]
liste des lettres essayé
nombre d'essai restant = 7

fonction de choisir
    demande choisir lettre
        si lettre ne fait pas partie de liste cachée
            nombre d'essai restant -1 
            ajoute à liste d'essai

        si lettre fait partie de la liste cachée 
            trouve indice de lettre choisi dans liste caché
            assigné l'indice dans la liste visible
            changé la lettre  dans l'indice avec la lettre choisi
            ajoute à liste d'essai
        répète demande choisir 
    si nombre d'essai restant = 0 
        arrête répète choisir
        affiche "game over"
        afficher le mot "exercice"



"""
"""while true:
    afficher le mot caché, les lettre utilisées et le nombre d'essais (SL)"""

while True:
    print(liste_mots_visible)
    print(liste_mots_utilisee)
    print(f"Il te reste {nombre_essai} essais")

"""
"""
# jessyka
# jacob-philip liste, if/elif , boucle, print, input

################chris Simpore#################
"""#1-lister les lettres des bons mots
#2-definir les boucles d'essaie 
#3-les condition if/elif
#4-

"""
# Fatoumata
# créer une liste de mots
# fixer un nombre maximum d'erreurcréer une liste de mots vide
# choisir un mot


# Fred
# Listes,if,elif,inputs,fonctions,print,boucle
# amar


# Sow.L
# ===================Lamarana===========================
"""
Mettre un liste de mots
Mettre la fonction input pour demander à l'utilisateur de choisir un mot



"""
import random

liste_mot = ["jouer", "python", "cocoluche", "boucle", ]
liste_mot.random.choise()

# Don Guylain Karl Irakoze
# Inputs, if, elif, fonctions, print, boucle
#

# Jonthan Demers
"""
motCherche
listeCharCherche = []
listeCache
lenListe = len(motCherche)



while i <= lenListe:

    listeCharCherche.append(motCherche[i])

    i += 1

"""

''' **jess** 
liste de mots:
ls_liste(): dadada desmots 
pendu: nombre d'essais
liste de lettres:
probs isalpha use, if not isalpha == False ddada
on veux pas de ## so ^^^^

ooo random.randint! yes indeed.
pour randomizer les mots dans la liste
on peut utiliser append aussi et len comme tou le monde sais.
ah c'es t vrais faut cacher les lettres et les faire apparaitre au fur et a mesure!
hmmmmmm

    .-------.
    |       |
    |
    |
    |
    |
[___|____________]

import random



def jeu(ls_mots, ls_alpha, vies, solution):
ls_mots: str([des mots on vas faire sa en équipe, right guys?])
ls_alpha: str(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) 
vies = 6 
solution = str('[ls_mots]')'''
'''
def pendu(5):
print('   .________.')
print('   |        |'
for p in range(4):
print('   |    ')
print('[__|_____________]')
    if vies == 4:
    print('   .________.')
    print('   |        |')
    print('   |        O')
    for p in range(3):
    print('   |    ')
    print('[__|_____________]')
    elif vie == 3:
    print('   .________.')
    print('   |        |')
    print('   |        O')
    print('   |       /|\,)      
    for p in range(2):
    print('   |    ')
    print('[__|_____________]')
    elif vie == 2:
    print('   .________.')
    print('   |        |')
    print('   |        O')
    print('   |       /|\')
    print('   |       /  ')
    for p in range(1):
    print('   |    ')
    print('[__|_____________]')
    elif vie == 1:
    print('   .________.')
    print('   |        |')
    print('   |        O')
    print('   |       /|\')
    print('   |       / \')
    for p in range(1):
    print('   |    ')
    print('[__|_____________]')
    else vie == 0:
    print('   .________.')
    print('   |        |')
    print('   |        X')
    print('   |       /|\')
    print('   |       / \')
    for p in range(1):
    print('   |    ')
    print('[__|_____________]')
    print('{solution} meilleur chance la prochaine fois!')
                                                            '''
'''

we must stop info1
wait who is info1
it could be me
it could be you
it could be any of us

>////<'
'''


