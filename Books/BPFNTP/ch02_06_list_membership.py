__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

print('Son-Huy' in 'Son-Huy TRAN')
print('Kha-Thy' in 'Kha-Thy NGO')
print('Son-Huy' in 'meo-map')
print('Kha-Thy' in 'meo-meo')
print(18 in [18, 25])

users = [
    ['Son-Huy TRAN', '1881'],
    ['Kha-Thy NGO', '9330']
]

username = input('Username: ')
pin = input('PIN code: ')

if [username, pin] in users:
    print('Access granted')
else:
    print('Unauthorized access')