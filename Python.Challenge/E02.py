__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://www.pythonchallenge.com/pc/def/map.html'
__version__ = '1.0'

import string

value = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb
gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq
pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

intab = string.ascii_lowercase
outtab = list(intab)

for i in range(len(outtab)):
    outtab[i] = intab[(i + 2) % len(intab)]

outtab = ''.join(outtab)

transtable = str.maketrans(intab, outtab)
print(value.translate(transtable))

url = "map"
print(url.translate(transtable))