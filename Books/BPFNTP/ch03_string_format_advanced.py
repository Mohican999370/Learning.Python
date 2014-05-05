__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

width = int(input('Please enter width: '))
price_width = 15
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print('=' * width)
print(header_format % (item_width, 'Item', price_width, 'Price'))
print('-' * width)
print(format % (item_width, 'Apples', price_width, 0.4))
print(format % (item_width, 'Pears', price_width, 0.5))
print(format % (item_width, 'Cantaloupes', price_width, 1.92))
print(format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8))
print(format % (item_width, 'Prunes (4 lbz.)', price_width, 12))
print('=' * width)