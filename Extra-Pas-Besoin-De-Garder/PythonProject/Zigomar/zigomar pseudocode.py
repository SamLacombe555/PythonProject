"""
- Fonctions à se partager:
# Commencer avec potion/cle/boule/squelette (sac commence avec 4 items)
# Ajout d'items dans le sac
# Retirer d'items dans le sac
# Liste/variable items (créer de nouveaux items en même temps)
# Fonction auto: Retirer SEULEMENT items qui contiennent un chiffre ou lettre B
# Fonction manuelle: Retirer un seul item qu'on choisi nous même
# Mini quiz : mélange sac, attrape objet par hasard, Zigomar devine et réagit (Choisir si ça sera une seule fonction ou 3)
    # Détecter si en ordre alphabétique et coder réaction Zigomar
    # Si pas en ordre alphabétique, fonction pour trier

#




- Pseudo -

# Choisir si la chasse se termine après un nombre défini de parties ou bien sur demande
# Inclure import random, random.shuffle(liste), random.choice(liste)

liste_item = 0


afficher_sac() # Afficher le contenu du sac et l'ordre des 15 items dedans après chaque opération
initialiser_sac() # Commencer avec potion/cle/boule/squelette (sac commence avec 4 items)
ajouter_objets() # Ajout d'items dans le sac
objet_a_retirer() # Retirer d'items dans le sac (avec liste)

# COMMANDES LISTE
sac.append(str)
sac.remove(str)
Random.shuffle(str)


# NOMS VARIABLES
sac
sac_filtré
nouveaux_objets





tri_auto() # Fonction auto: Retirer SEULEMENT items qui contiennent un chiffre ou lettre B
tri_manuel() # Fonction manuelle: Retirer un seul item qu'on choisi nous même


mini_quiz()

tri_final() # Si pas en ordre alphabétique, fonction pour trier
"""

# Section William

import random

# Initialisation du sac avec les objets de départ
def initialiser_sac():
    return [
        "potion scintillante",
        "clé mystérieuse",
        "boule brillante",
        "squelette miniature"
    ]

# Ajout de nouveaux objets au sac
def ajouter_objets(sac, nouveaux_objets):
    for objet in nouveaux_objets:
        sac.append(objet)
    return sac

# Tri automatique : retire les objets contenant un chiffre ou la lettre "b"
def tri_automatique(sac):
    sac_filtré = []
    for objet in sac:
        if not any(c.isdigit() or c.lower() == 'b' for c in objet):
            sac_filtré.append(objet)
    return sac_filtré

# Fin de la section William
# (Version 1.1)

# Section Sam

def melanger_sac(sac: list[str]):
    sac_melange = random.shuffle(sac)
    return sac_melange

def attraper_objet(sac: list[str]):
    objet_attrape = random.choice(sac)
    return objet_attrape

def deviner_objet(sac:list[str]):
    objet_devine = random.choice(sac)
    return objet_devine

def reaction_deviner(objet_attrape:str, objet_devine:str):
    if objet_attrape == objet_devine:
        print("Yoopie! J'ai gagnée! Merci d'avoir jouer avec moi.")
    if objet_attrape != objet_devine:
        print("Hmm. Peu importe...")

def reaction_maniaque(sac:list[str]):
    sac = sac.sort()
    print("ARGH! Mon sac est tout désorganisé! Tu dois tout replacer en ordre alphabétique!")
    return sac
