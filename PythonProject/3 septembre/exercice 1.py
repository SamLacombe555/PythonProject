def nouveau_adresse_courriel(prénom, nom):

    return f"{prénom}.{nom}@cegepoutaouais.qc.ca"

def demande_prénom():
    prénom=str(input("Quelle est votre prénom?"))
    return prénom

def demande_nom():
    nom=str(input("Quelle est votre nom?"))
    return nom

demande_prénom()
demande_nom()


print(nouveau_adresse_courriel(prénom, nom))
