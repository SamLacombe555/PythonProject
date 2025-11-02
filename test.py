try:
    nombre = int(input("Entrez un nombre:"))
    resultat = 10 / nombre
except ValueError:
    print("La valeur entrée n'est pas un nombre")
except ZeroDivisionError:
    print("La valeur entrée ne doit pas être 0!")
except:
    print("Une erreur est survenue")
else:
    print(resultat)
finally:
    print("Fin!")