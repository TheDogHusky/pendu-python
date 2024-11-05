import utils
from game import handle_game

def main():
    replay = True
    # Tant que l'utilisateur veut jouer, on relance le jeu
    while replay:
        mot = input(utils.format_log("WARNING", "Quel est le mot?: "))
        if not utils.is_word(mot):
            utils.log("FAIL", "Erreur: Le mot entré n'est pas un mot valide.")
            continue
        mot = mot.upper()
        # On initialise les variables
        lettres_fausses = []
        guessed = False
        lettres_trouvees = []
        # On gère le jeu !
        while not guessed:
            guessed = handle_game(mot, lettres_fausses, lettres_trouvees)
        replay = utils.confirm(utils.format_log("WARNING", "Voulez-vous rejouer? (Y/N): "))


# Entourer le programme dans une fonction main avec cette condition permet d'éviter l'exécution du code si on importe le fichier. C'est une convention.
if __name__ == "__main__":
    main()