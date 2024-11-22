import utils

tries_per_difficulty = {
    0: 12,
    1: 8,
    2: 6
}

# Fonction permettant de gérer le jeu. Retourne un booléen si on a trouvé le mot ou pas
def handle_game(mot, lettres_fausses, lettres_trouvees, difficulty):
    max_tries = tries_per_difficulty[difficulty]
    utils.log("green", "Mot: " + utils.underscorize(mot, lettres_trouvees))
    utils.log("green", f"Essais ratés: {", ".join(lettres_fausses)} (encore {max_tries - len(lettres_fausses)})")
    guess = utils.styled_input("yellow", "Prochaine lettre (ou mot)?: ")
    # On vérifie que l'entrée est un mot ou une lettre correcte
    if not utils.is_word(guess):
        utils.log("red", "Le mot ou la lettre entré(e) n'est pas valide (hors jeu).")
        return False
    # On met l'entrée en majuscules pour pouvoir la comparer correctement
    guess = guess.upper().strip()
    # Si l'entrée est dans le mot
    if guess in list(mot):
        # On vérifie que l'entrée n'a pas déjà été trouvée
        if guess in lettres_trouvees:
            utils.log("yellow", "Tu as déjà trouvé cette lettre!")
            return False
        # Si la lettre est valide, on l'ajoute dans les lettres trouvées
        utils.log("green", "Lettre valide !")
        lettres_trouvees.append(guess)
        # Si c'était la dernière lettre à trouver, on finit le jeu
        if utils.is_same(mot, lettres_trouvees):
            utils.print_win(lettres_fausses, mot)
            return True
        return False
    # Si l'entrée est déjà dans les lettres fausses, et que la difficulté n'est pas difficile, alors on le dit à l'utilisateur
    if guess in lettres_fausses and difficulty != 2:
        utils.log("yellow", "Tu as déjà tenté cette lettre!")
        return False
    # Si l'entrée est le mot, on finit le jeu
    if guess == mot or utils.is_same(mot, lettres_trouvees):
        utils.print_win(lettres_fausses, mot)
        return True
    # Si toutes ces conditions ont raté, on ajoute l'entrée dans les lettres fausses et on renvoie à l'utilisateur son erreur
    lettres_fausses.append(guess)
    if len(lettres_fausses) >= max_tries:
        utils.log("red", "Tu as perdu!")
        utils.log("red", f"Le mot était {mot}")
        # On renvoie true (donc mot trouvé) car c'est la façon la plus optimisée de stopper le jeu
        return True
    utils.log("red", f"Raté, tu as encore {max_tries - len(lettres_fausses)} essais !")
    # S'il n'a plus d'essais disponibles, on arrête le jeu
    return False