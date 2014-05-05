__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

name = list('Perl')
print('before:', ''.join(name))
name[2:] = list('ar')
print('after:', ''.join(name), '\n')

python = list('Perl')
print('before:', ''.join(python))
python[1:] = list('ython')
print('after:', ''.join(python), '\n')

numbers = [1, 5]
print('before:', numbers)
numbers[1:] = [2, 3, 4]
print('after:', numbers, '\n')