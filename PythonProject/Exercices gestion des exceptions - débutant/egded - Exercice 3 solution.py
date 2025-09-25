
# ******************* Réponses aux questions de l'exercice ******************* #
# Exécutez-le et lisez l'erreur.
#       AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
# Quel est le type d'exception? Qu'est-ce que cela signifie ?
#       Type d'exception : AttributeError
#       Signification : Une liste n'a pas d'attribut (ici il s'agit d'une fonction native) appelé sorted().
#                      Fonction native proposée : sort().
# Que faut-il faire dans ce cas, gérer l'exception ou corriger l'erreur ?
#       Mettre liste.sort() à la place de liste.sorted()
# **************************************************************************** #

def trier_liste(liste: list) -> None :
    """
    Cette fonction trie la liste passée en paramètres.
    :param liste: liste à trier.
    :return: (Aucun).
    """
    # Correction 2 (en extra) : On gère l'exception où la valeur qu'on passe à cette fonction n'est pas une liste.
    try:
        # Correction 1 : sort() à la place de sorted()
        liste.sorted()
        print(liste_nums)
    except AttributeError:
        print(f"{liste_nums} ne peut pas être triée. La valeur passée à la fonction trier_liste doit être une liste.")

if __name__ == "__main__":
    liste_nums = [8, 7, 1, 5, 4]
    trier_liste(liste_nums)