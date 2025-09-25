def ajouter_points(score, points):
    """
    Ajoute des points au score existant.
    """
    score = score + points
    return score

def est_haut_score(score):
    """
    Retourne True si le score est supérieur ou égal à 100, sinon False.
    """
    if score >= 100:
        haut_score = True
    else:
        haut_score = False

    return haut_score

if __name__ == "__main__":
    score1 = 70
    score2 = 95

    nouveau_score1 = ajouter_points(score1, 20)
    nouveau_score2 = ajouter_points(score2, 10)

    haut1 = est_haut_score(nouveau_score1)
    haut2 = est_haut_score(nouveau_score2)

    print(f"Joueur 1 : {nouveau_score1} points, haut score ? {haut1}")
    print(f"Joueur 2 : {nouveau_score2} points, haut score ? {haut2}")
