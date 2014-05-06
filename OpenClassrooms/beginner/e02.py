__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = """
Pour commencer l'ordinateur va choisir au hasard un nombre compris entre 1 et 100.
L'utilisateur doit alors deviner ce nombre comme ceci :
L'utilisateur propose un nombre.
L'ordinateur lui dit s'il est trop petit ou trop grand,
et ainsi de suite jusqu'à ce que l'utilisateur aie trouvé le bon nombre.
"""
__version__ = '1.0'

import random

value = random.randrange(1, 100)
guess = 0
tries = 0

while (guess != value):
    try:
        guess = int(input('Quel est le nombre ? '))
    except ValueError:
        guess = 0
        print("Ceci n'est pas un nombre.")
        continue

    tries += 1

    if (guess == value):
        print('Félicitations, vous avez trouvé le nombre mystère après %d essais !!!' % tries)
    elif (guess < value):
        print("C'est trop petit !")
    else:
        print("C'est trop grand !")