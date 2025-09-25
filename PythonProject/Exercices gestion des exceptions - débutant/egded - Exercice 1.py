def division(nombre_1:int, nombre_2:int) -> float:
    """
    Fonction qui prend deux nombre entier, les divise et les arrondissent
    :param nombre_1: Premier nombre
    :param nombre_2: Deuxième nombre
    :return: Résultat de la division
    """

    try:
        resultat_division = round(nombre_1/nombre_2)
        return resultat_division

    except ZeroDivisionError:
        return None

    except TypeError:
        print("Les nombres doivent être entiers")
        return None

if __name__ == "__main__":

    try:
        entree_1 = int(input("Entrez le premier nombre"))
        entree_2 = int(input("Entrez le deuxième nombre"))

        res_division = round(division(entree_1, entree_2))
        if res_division is None:
            print("Impossible de diviser")
        else:
            print(f"Le résultat de la division entre {entree_1} et {entree_2} est {res_division}")


    except ValueError:
        print("Les nombres doivent être entier")
