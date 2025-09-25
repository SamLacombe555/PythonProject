ls_couleur = ["bleu", "jaune", "rouge", "vert", "bleu", "jaune"]
print("0. ",ls_couleur)

ls_couleur.pop(1)
ls_couleur.insert(1,"rouge")
print("3. ",ls_couleur)

ls_couleur.append("vert")
print("4. ",ls_couleur)

ls_couleur.insert(2, "bleu")
print("5. ",ls_couleur)

ls_couleur.append("bleu")
ls_couleur.append("vert")
print("6. ",ls_couleur)

ls_couleur.remove("bleu")
print("7. ",ls_couleur)

ls_couleur.pop(4)
print("8. ",ls_couleur)

print("9. ",ls_couleur.index("vert"))

print("10. ", len("vert"))

ls_couleur.sort()
print("11. ", ls_couleur)

ls_couleur.sort(reverse=True)
print("12. ",ls_couleur)
