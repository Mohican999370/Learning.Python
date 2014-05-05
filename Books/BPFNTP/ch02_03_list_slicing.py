__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

tag = '<a href="http://www.sonhuythedev.com">Son-Huy TRAN: A developer\'s blog</a>'

print(tag[9:36])
print(tag[38:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('[7:10]: ', numbers[7:10])
print('[-3:-1]: ', numbers[-3:-1])
print('[-3:0]: ', numbers[-3:0])
print('[-3:]: ', numbers[-3:])
print('[:3]: ', numbers[:3])
print('[:]: ', numbers[:])
print('[0:10:1]: ', numbers[0:10:1])
print('[0:10:2]: ', numbers[0:10:2])
print('[::4]: ', numbers[::4])
print('[10:0:-2]: ', numbers[10:0:-2])
print('[::-4]', numbers[::-4])
print('[:5:-2]', numbers[:5:-2])