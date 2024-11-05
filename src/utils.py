# Fonction permettant de vérifier si une variable est un mot (alphabétique)
def is_word(s):
    # On vérifie que le type de la variable est bien un string, et que ce string est alphabétique
    return type(s) == str and (s.replace("-", "")).isalpha()

# Fonction permettant de faire une confirmation avec input()
def confirm(question):
    # On n'arrête pas de poser la question tant que la réponse n'est pas une confirmation valide
    while True:
        # On demande à l'utilisateur si in veut "question"
        answer = input(question)
        if not is_confirmation(answer):
            # Si l'entrée n'est pas "Y" ou "N", on lui redemande
            print(":: Entrée invalide. Merci d'entrer Y ou N")
            continue
        else:
            # On retourne un booléen : si la réponse est Y, alors c'est une confirmation
            return answer == "y"

# Fonction permettant de vérifier si une entrée est une confirmation (donc N ou Y)
def is_confirmation(s):
    answers = ["y", "n"]
    # On vérifie si l'entrée est un string, et si c'est Y ou N (la fonction strip() "nettoie" l'entrée, retire les espaces.
    return type(s) == str and (s.strip())[0].lower() in answers

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

colors = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}

def format_log(log_type, message):
    return colors[log_type] + colors["BOLD"] + ":: " + colors["ENDC"] + message + colors["ENDC"]

def log(log_type, message):
    print(format_log(log_type, message))
