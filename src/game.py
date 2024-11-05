import utils

# Fonction permettant de gérer le jeu. Retourne un booléen si on a trouvé le mot ou pas
def handle_game(mot, lettres_fausses, lettres_trouvees):
    utils.log("OKGREEN", "Mot: " + utils.underscorize(mot, lettres_trouvees))
    utils.log("OKGREEN", f"Essais ratés: {lettres_fausses} (encore {8 - len(lettres_fausses)})")
    guess = input(utils.format_log("WARNING", "Prochaine lettre (ou mot)?: "))
    if not utils.is_word(guess):
        utils.log("FAIL", "Le mot ou la lettre entré(e) n'est pas valide (hors jeu).")
        return False
    if guess in list(mot):
        utils.log("OKGREEN", "Lettre valide !")
        lettres_trouvees.append(guess.strip())
        return False
    if guess == mot:
        utils.log("OKGREEN", "Bravo, tu as trouvé le mot !")
        utils.log("OKGREEN", f"Après {len(lettres_fausses)} fausses lettres !")
        return True
    utils.log("FAIL", f"Raté, tu as encore {8 - len(lettres_fausses)} essais !")
    return False