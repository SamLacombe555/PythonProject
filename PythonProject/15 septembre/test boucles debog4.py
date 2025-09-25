def les_listes(n):
    resultat = []
    while n > 0:
        resultat.append(n)
        n = n - 2
    return resultat

les_listes(10)