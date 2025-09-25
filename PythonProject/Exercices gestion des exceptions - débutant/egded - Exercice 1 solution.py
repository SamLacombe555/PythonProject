def division(nombre1: int, nombre2: int) -> float:
    """
    Cete fonction fait la division entre les deux nombres
    passés en paramètres et retourne le résultat.
    :param nombre1: Le 1er nombre entier.
    :param nombre2: Le 2ème nombre entier.
    :return: Le résultat de division entre nombre1 et nombre2
    """
    try:
        resultat_division = round(nombre1 / nombre2)
        return resultat_division

    except ZeroDivisionError:
        return None

    except TypeError:
        print("Les deux nombres doivent être des entiers")
        return None


if __name__ == "__main__":

    try:
        nb1 = int(input("Veuillez entrer le 1er nombre entier : "))
        nb2 = int(input("Veuillez entrer le 2ème nombre entier : "))
        res_division = round(division(nb1, nb2))
        if res_division is None:
            print("Impossible de faire une division par zéro.")
        else:
            print(f"Le résultat de la division entre {nb1} et {nb2} est égal à {res_division}")

    except ValueError:
        print("Les deux nombres doivent être des entiers")
