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