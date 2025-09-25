def retrait(solde:float = 0, retrait: float = 0) -> bool:
    if retrait > solde:
        retrait = solde
        print(f"* Solde insuffisant, retrait effectué: {retrait} $")

def

    solde = solde - retrait
    print(f"* Retrait effectué: {retrait}")

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
    print(f"Solde final:    {solde} $")
    print(f"*********************")