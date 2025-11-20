"""
- MASTERMIND_main.py est le programme principal à exécuter.
- MASTERMIND_fonctions.py contient toutes les fonctions qu'utilise le programme.
- SectionWilliam.py et mini_projet_test_sam.py délimitent qui a fait quoi.
- PlansDeTests.md, TestsUnitaires.py et Échéancier.md sont ce qu'ils disent être.
- plan_mini_projet.py contient un pré-pseudocode. Le vrai pseudocode se trouve dans MASTERMIND_main.py et MASTERMIND_fonctions.py
- Vous vous trouvez actuellement dans README.py
"""

"""
- Maryse Mongeau -
Le projet est bien commencé. Mais il doit être mieux organisé.
Nettoyer le repository sur GitHub, il contient des fichiers qui ne font pas partie du projet.
Il y a aussi des parties qui semblent dédoublées, je ne sais pas lesquelles regarder.
Organiser le code utile dans un ou des fichiers de modules pour les fonctions, et un fichier pour le programme principal.
"""

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"  # Reset to default color

# Create a list with colored strings
colored_list = [
    f"{RED}Apple{RESET}",
    f"{GREEN}Banana{RESET}",
    f"{BLUE}Blueberry{RESET}"
]

# Print each element
for item in colored_list:
    print(item)

# You can still access the raw string with color codes
print("\nRaw list data:", colored_list)
