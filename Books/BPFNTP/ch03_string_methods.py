__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

import string

# string module's constants
print('digits:', string.digits)
print('hexadecimal digits:', string.hexdigits)
print('octal digits:', string.octdigits)
print('letters:', string.ascii_letters)
print('lowercase:', string.ascii_lowercase)
print('uppercase:', string.ascii_uppercase)
print('punctuation:', string.punctuation)
print('printable:', string.printable)
print('whitespace:', string.whitespace)

# find() method
title = 'Son-Huy the Developer'
print('title =', title)
print('index of \'Son-Huy\' =', title.find('Son-Huy'))
print('index of \'Developer\' =', title.find('Developer'))
print('index of \'Meo Mập\' =', title.find('Meo Mập'), '\n')

# join() method
print('/'.join(['user', 'lib', 'python', '']), '\n')

# lower() & upper() method
print('lowercase:', 'Son-Huy TRAN'.lower())
print('uppercase:', 'Son-Huy TRAN'.upper(), '\n')

# replace() & split() method
my_string = '   Meo Mập   '
print('before:', my_string)
my_string = my_string.strip()
print('after stripping:', my_string)
my_string = my_string.replace('Mập', 'Bự')
print('after replacing:', my_string)
print('after splitting by a space:', my_string.split(' '))

# maketrans
translation_table = str.maketrans('M', 'B')
print('after translation:', my_string.translate(translation_table))