__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
__version__ = '1.0'

from urllib import request
import re

nothing = 12345

for i in range(400):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing
    response = request.urlopen(url).read().decode('utf8')
    matches = re.findall('[0-9]+', response)

    if (len(matches) > 0):
        nothing = matches[0]
        print('nothing =', nothing)
    elif (response == 'Yes. Divide by two and keep going.'):
        nothing = int(nothing) % 2
        print('nothing =', nothing)
    else:
        print('Not matched. Found:', response)
        break