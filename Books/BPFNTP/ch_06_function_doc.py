__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

def say_hello(name):
    'Print out a Hello sentence'
    print('Hello', name, '!!!')

print(say_hello.__doc__)
help(say_hello)