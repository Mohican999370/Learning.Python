__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = """
01. Constituez une liste semaine contenant les 7 jours de la semaine.
A partir de cette liste, comment récupérer seulement les cinq premiers jours de la semaine d'une part
et ceux du week-end d'autres part (en utilisant l'indiçage)?
cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).

02. Trouvez 2 manières pour accéder au dernier jour de la semaine.

03. Inversez les jours de la semaine en une seule commande python.
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

# Exercise 01
print('01. Première méthode'.upper())
semaine = jours[:5]
week_end = jours[5:]
print('Cinq jours de la semaine :', ', '.join(semaine))
print('Les jours du week-end :', ', '.join(week_end), '\n')

print('01. Seconde méthode'.upper())
semaine = jours[-7:-2]
week_end = jours[-2:]
print('Cinq jours de la semaine :', ', '.join(semaine))
print('Les jours du week-end :', ', '.join(week_end), '\n')

# Exercise 02
print('02. Première méthode'.upper())
dernier = jours[6]
print('Le dernier jour de la semaine :', dernier, '\n')

print('02. Seconde méthode'.upper())
dernier = jours[-1]
print('Le dernier jour de la semaine :', dernier, '\n')

# Exercise 03
print('03.')
print('Les jours de toute la semaine dans l\'ordre inverse:', ', '.join(list(reversed(jours))))