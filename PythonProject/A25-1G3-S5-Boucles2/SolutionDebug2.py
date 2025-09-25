def retrait(solde: float, montant: float) -> float:
    """
    Effectue un retrait sur le solde donné.

    - Si le montant est négatif ou nul, le retrait est refusé.
    - Si le montant est supérieur au solde, on retire seulement le solde restant.
    - Sinon, on retire le montant demandé.

    Retourne le nouveau solde.
    """
    if montant <= 0:
        print("* Retrait refusé (montant invalide)")
        return solde

    if montant > solde:
        print(f"* Solde insuffisant, retrait effectué: {solde} $")
        return 0  # tout le solde est retiré

    solde -= montant
    print(f"* Retrait effectué: {montant} $")
    return solde


if __name__ == "__main__":
    MONTANT_INITIAL = 1000
    solde = MONTANT_INITIAL

    print("*************************")
    print("***      GUICHET      ***")
    print("*************************")
    print(f"Solde initial:  {solde} $")
    print("*************************")

    retrait_1 = float(input("Retrait 1: Combien voulez-vous retirer? "))
    solde = retrait(solde, retrait_1)

    retrait_2 = float(input("Retrait 2: Combien voulez-vous retirer? "))
    solde = retrait(solde, retrait_2)

    print("*********************")
    print(f"Solde initial: {MONTANT_INITIAL} $")
    print(f"Retrait 1:     {retrait_1} $")
    print(f"Retrait 2:     {retrait_2} $")
    print(f"Solde final:   {solde} $")
    print("*********************")
