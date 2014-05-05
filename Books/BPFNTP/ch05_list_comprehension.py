__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

print([x * x
       for x in range(10)])
print([x * x
       for x in range(10)
       if x % 3 == 0])
print([(x, 2 * x)
       for x in range(10)])
print([(x, y)
       for x in range(3)
       for y in range(2)])