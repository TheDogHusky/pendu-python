import numpy as np
import os
from rich import print

# Fonction permettant de vérifier si une variable est un mot (alphabétique)
def is_word(s):
    # On vérifie que le type de la variable est bien un string, et que ce string est alphabétique
    return type(s) == str and (s.replace("-", "")).isalpha()

# Fonction permettant de faire une confirmation avec input()
def confirm(question):
    # On n'arrête pas de poser la question tant que la réponse n'est pas une confirmation valide
    while True:
        # On demande à l'utilisateur si in veut "question"
        answer = styled_input("yellow", question)
        if not is_confirmation(answer):
            # Si l'entrée n'est pas "Y" ou "N", on lui redemande
            log("red", "Entrée invalide. Merci d'entrer Y ou N")
            continue
        else:
            # On retourne un booléen : si la réponse est Y, alors c'est une confirmation
            return answer == "y"

# Fonction permettant de vérifier si une entrée est une confirmation (donc N ou Y)
def is_confirmation(s):
    answers = ["y", "n"]
    # On vérifie si l'entrée est un string, et si c'est Y ou N (la fonction strip() "nettoie" l'entrée, retire les espaces.
    return type(s) == str and len(s) != 0 and (s.strip())[0].lower() in answers

# Utilisée pour transformer un mot en un mot à deviner pour le pendu
# Exemple: "adam" -> "_ _ _ _" selon les lettres trouvées
def underscorize(mot, lettres_trouvees):
    # On transforme toutes les lettres en underscore, sauf celles trouvées
    underscored = ""
    # On itère sur toutes les lettres
    for letter in mot:
        # Si elle fait partie des lettres trouvées, on la transforme pas
        if letter in lettres_trouvees:
            underscored += letter
        else:
            # Sinon on la transforme
            underscored += "_"
        underscored += " "
    return underscored


# Permet de formatter le message à afficher dans la console (ajout des couleurs et des décorations)
def format_log(log_type, message):
    return f"[bold {log_type}]::[/] {message}"

# Permet d'afficher un message dans la console avec des couleurs et décorations
def log(log_type, message):
    print(format_log(log_type, message))

# Permet d'afficher le message de victoire dans la console
def print_win(lettres_fausses, mot):
    clear()
    log("green", "Bravo, tu as trouvé le mot !")
    log("green", f"Le mot était {mot} !")
    log("green", f"Après {len(lettres_fausses)} fausse(s) lettre(s) !")

# Si les lettres trouvées couvrent toutes les lettres du mot
def is_same(mot, lettres_trouvees):
    mot = np.unique(list(mot))
    # On regarde donc si les lettres contenues dans lettres_trouvees sont égales aux lettres contenues dans mot en comparant leur version rangée
    return sorted(mot) == sorted(lettres_trouvees)

# Permet d'effacer la console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Permet de vérifier si une entrée est une difficulté valide
def is_difficulty(entry):
    valid_entries = ["f", "n", "d", "i"]
    return type(entry) == str and len(entry) != 0 and (entry.strip())[0].lower() in valid_entries

# Permet de transformer une difficulté (en chaîne de caractères) en nombre
def parse_difficulty(entry):
    definition = {
        "f": 0,
        "n": 1,
        "d": 2,
        "i": 3
    }

    return definition[entry]

# Permet d'effectuer un input avec les couleurs.
# Dû au fait que la librairie que nous utilisons utilise un print spécifique et qu'on ne peut pas changer la méthode de print dans une input
def styled_input(color, message):
    # On print avec la fonction du module rich, sans saut à la ligne
    print(format_log(color, message), end="")
    # Puis on fait une input vide
    return input("")