import utils

# TODO faire des modes de difficulté (nbr d'essais et tolérence avec les erreurs déjà trouvées

# Fonction permettant de gérer le jeu. Retourne un booléen si on a trouvé le mot ou pas
def handle_game(mot, lettres_fausses, lettres_trouvees):
    utils.log("OKGREEN", "Mot: " + utils.underscorize(mot, lettres_trouvees))
    utils.log("OKGREEN", f"Essais ratés: {", ".join(lettres_fausses)} (encore {8 - len(lettres_fausses)})")
    guess = input(utils.format_log("WARNING", "Prochaine lettre (ou mot)?: "))
    # On vérifie que l'entrée est un mot ou une lettre correcte
    if not utils.is_word(guess):
        utils.log("FAIL", "Le mot ou la lettre entré(e) n'est pas valide (hors jeu).")
        return False
    # On met l'entrée en majuscules pour pouvoir la comparer correctement
    guess = guess.upper().strip()
    # Si l'entrée est dans le mot
    if guess in list(mot):
        # On vérifie que l'entrée n'a pas déjà été trouvée
        if guess in lettres_trouvees:
            utils.log("WARNING", "Tu as déjà trouvé cette lettre!")
            return False
        # Si la lettre est valide, on l'ajoute dans les lettres trouvées
        utils.log("OKGREEN", "Lettre valide !")
        lettres_trouvees.append(guess)
        # Si c'était la dernière lettre à trouver, on finit le jeu
        if utils.is_same(mot, lettres_trouvees):
            utils.print_win(lettres_fausses, mot)
            return True
        return False
    # Si l'entrée est le mot, on finit le jeu
    if guess == mot or utils.is_same(mot, lettres_trouvees):
        utils.print_win(lettres_fausses, mot)
        return True
    # Si toutes ces conditions ont raté, on ajoute l'entrée dans les lettres fausses et on renvoie à l'utilisateur son erreur
    lettres_fausses.append(guess)
    if len(lettres_fausses) == 8:
        utils.log("FAIL", "Tu as perdu!")
        utils.log("FAIL", f"Le mot était {mot}")
        # On renvoie true (donc mot trouvé) car c'est la façon la plus optimisée de stopper le jeu
        return True
    utils.log("FAIL", f"Raté, tu as encore {8 - len(lettres_fausses)} essais !")
    # S'il n'a plus d'essais disponibles, on arrête le jeu
    return False