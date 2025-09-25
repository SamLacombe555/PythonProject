#   chq astronautes pèsent 80kg
#   chq modules spatiaux pèsent 500kg
#   montant de carburant dépant du poids et d'un facteur de consommation de 2L/kg
#   si VIP, bonus carburant
#   tempête solaire = mauvais
#   je nomme la mission en majuscule et centré dans le rapport

nombre_astronaute = float(input("Il y a combien d'astronaut?"))
masse_astronaute = nombre_astronaut * 80
nombre_module = float(input("Il y a combien de modules disponibles?"))
masse_module = nombre_module *500
masse_totale = masse_astronaute + masse_module
carburant_besoin = masse_totale * 2
vip = bool(int(input("Est-ce que l'organisateur est VIP?")))
carburant_vip = carburant_besoin + (50*vip)
carburant_actuel = int(input("Combien de carburant est disponible?"))
realisable = carburant_actuel >= carburant_vip
tempete = bool(int(input("Est-ce qu'il y a une tempête solaire?")))



print(f"Astronaute : {nombre_astronaute} (masse totale {masse_astronaute} kg")
print(f"Modules disponibles : {nombre_module} (masse totale {masse_module} kg")
print(f"Masse totale du vaisseau : {masse_totale} kg")
print(f"Carburant nécessaire: {carburant_besoin} litres")
