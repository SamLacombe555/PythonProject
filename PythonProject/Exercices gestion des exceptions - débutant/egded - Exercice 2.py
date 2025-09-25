def permute_liste(liste : list, i : int, j : int):
    """
    Fonction qui change la position entre deux éléments
    :param liste: Liste contenant les éléments
    :param i: indice du premier élément
    :param j: indice du deuxième élément
    :return: La nouvelle liste avec les éléments échangés
    """

    liste[i], liste[j] = liste[j], liste[i]
    return liste

if __name__ == "__main__":
    liste = [1,2,3,4,5,6]
    print(f"")


    indice_1 = 2
    indice_2 = 3