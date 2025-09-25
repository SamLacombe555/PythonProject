"""
Pseudocode de la fonction :
FONCTION defense_serveur(cryptage, scripts, connaissances, logiciels)

		bonus_defence <- 3
		penalite_defence <- 2
		bonus_hacker <- 4

		// Calcul de la défense d'Eliot
		defense <- cryptage + scripts

		SI defense >= 15 ALORS
			defense <- defense + bonus_defence
		SINON
			defense <- defense - penalite_defence
		FINSI

		// Calcul de l'attaque du hacker
		attaque <- connaissances + logiciels

		SI connaissances >= 7 ET logiciels >= 7 ALORS
			attaque <- attaque + bonus_hacker
		FINSI

		// Comparaison
		resultat <- defense >= attaque

		RETOURNER resultat
FIN FONCTION
"""

def defense_serveur(cryptage, scripts, connaissances, logiciels):
    """
    Cette fonction détermine si la défense est suffisante pour protéger le serveur contre le hacker
    :param cryptage: Niveau de cryptage de la défense
    :param scripts: Qualité des scripts de la défense
    :param connaissances: Niveau de connaissances du hacker
    :param logiciels: Le nombre de logiciels du hacker
    :return: Résultat de la défense contre l'attaque
    """

    bonus_defense = 3
    penalite_defense = 2
    bonus_hacker = 4

    #Calcul de la défense d'Eliot
    defense = cryptage + scripts
    if defense >= 15:
        defense = defense + bonus_defense
    else:
        defense = defense - penalite_defense

    #Calcul de l'attaque du hacker
    attaque = connaissances + logiciels
    if connaissances >= 7 and logiciels >= 7:
        attaque = attaque + bonus_hacker

    #Comparaison
    resultat = defense >= attaque
    return resultat


print("Simulation de défense")
while True: #Répète si les valeurs sont refusées
    #Demande les valeurs
    niveau_cryptage = int(input("Quel est le niveau de cryptage de la défense d'Elliot?"))
    qualite_scripts = int(input("Quelle est la qualité des scripts de la défense d'Elliot?"))
    connaissance_hacker = int(input("Quel est le niveau de connaissances du hacker?"))
    logiciel_hacker = int(input("Combien de logiciels sont utilisés par le hacker?"))

    #Évalue si les valeurs sont acceptables
    if niveau_cryptage > 0 and niveau_cryptage <= 10 and qualite_scripts > 0 and qualite_scripts <= 10 and connaissance_hacker > 0 and connaissance_hacker <= 10 and logiciel_hacker >0 and logiciel_hacker <=10:
        break
    else:
        print("Erreur")

#Affiche résultat
print(defense_serveur(niveau_cryptage, qualite_scripts, connaissance_hacker, logiciel_hacker))

"""
if defense_serveur(niveau_cryptage,qualite_scripts,connaissance_hacker,logiciel_hacker) == True:
    resultat_simulation = "Le serveur s'est défendu de l'attaque"
else:
    resultat_simulation = "Le serveur a faillie de se défendre de l'attaque"
print(resultat_simulation)
"""
