__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = """
Constituez une liste semaine contenant les 7 jours de la semaine.
A partir de cette liste, comment récupérer seulement les cinq premiers jours de la semaine d'une part
et ceux du week-end d'autres part (en utilisant l'indiçage)?
cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).
"""
__version__ = '1.0'

jours = [
    'Lundi',
    'Mardi',
    'Mercredi',
    'Jeudi',
    'Vendredi',
    'Samedi',
    'Dimanche'
]

semaine = jours[:5]
week_end = jours[5:]

print('Première méthode'.upper())
print('Cinq jours de la semaine:', ', '.join(semaine))
print('Les jours du week-end:', ', '.join(week_end), '\n')

semaine = jours[-7:-2]
week_end = jours[-2:]

print('Seconde méthode'.upper())
print('Cinq jours de la semaine:', ', '.join(semaine))
print('Les jours du week-end:', ', '.join(week_end), '\n')