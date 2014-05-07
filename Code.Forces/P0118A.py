__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/118/A'
__version__ = '1.0'

import re
value = input().lower()
vowels = '[aeiouy]'
result = re.sub(vowels, '', value)

if result:
    print('.' + '.'.join(result))
else:
    print('')