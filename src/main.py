import utils
from game import handle_game
from time import sleep
import pyfiglet
from rich.text import Text

def main():
    print(pyfiglet.figlet_format("Python Pendu"))
    print(Text.assemble("Par Adam Billard, Owen Fouillet et Naoharu Takigawa", "cyan bold"))
    replay = True
    # Tant que l'utilisateur veut jouer, on relance le jeu
    while replay:
        mot = input(utils.format_log("yellow", "Quel est le mot?: "))
        # Si l'entrée n'est pas un mot, on le dit à l'utilisateur
        if not utils.is_word(mot):
            utils.log("red", "Erreur: Le mot entré n'est pas un mot valide.")
            continue
        difficulty = input(utils.format_log("yellow", "Quelle sera la difficulté? (F/Facile, N/Normal, D/Difficile): "))
        # Si l'entrée n'est pas une difficulté, on le dit à l'utilisateur
        if not utils.is_difficulty(difficulty):
            utils.log("red", "Erreur: La difficulté entrée n'est pas valide.")
            continue
        # On transforme la difficulté en nombre
        difficulty = utils.parse_difficulty(difficulty)
        # On met le mot en majuscules pour pouvoir le comparer
        mot = mot.upper()
        # On initialise les variables
        lettres_fausses = []
        guessed = False
        lettres_trouvees = []
        index = 0
        # On gère le jeu !
        while not guessed:
            if index != 0:
                sleep(1)
            utils.clear()
            guessed = handle_game(mot, lettres_fausses, lettres_trouvees, difficulty)
            index += 1
        replay = utils.confirm(utils.format_log("yellow", "Voulez-vous rejouer? (Y/N): "))


# Entourer le programme dans une fonction main avec cette condition permet d'éviter l'exécution du code si on importe le fichier. C'est une convention.
if __name__ == "__main__":
    main()