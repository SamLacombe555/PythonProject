def trier_liste(liste: list) -> None :
    try :
        liste.sorted()
        print(liste_nums)
    except AttributeError:
        


if __name__ == "__main__":
    liste_nums = [6, 3, 5, 2, 4, 1]
    trier_liste(liste_nums)
    print(liste_nums)