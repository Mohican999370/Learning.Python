__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

phones = {
    'Meo Mập': '2023',
    'Meo Bự': '9330'
}

# equivalent to:
# phones = dict('Meo Mập' = '2023', 'Meo Bự' = '9330')
# phones = dict([('Meo Mập', '2023'), ('Meo Bự', '9330')])

search = input('Who you are searching for? ')

if (search in phones):
    print('Phone number of', search, 'is', phones[search])
else:
    print('This person is not found in the phone book.\nAvailable entries are:',
          ', '.join(phones.keys()),
          sep='\n')