__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

import math
from string import Template

format = "Hello %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)

format = "PI with three decimals: %.3f"
print(format % math.pi)

format = "PI with other formats: %10f, %010f, %10.2f, %-10.2f"
print(format % ((math.pi,) * 4))

template = Template("It's $$${x}tastic$$")
print(template.substitute(x='fan'))

template = Template("A $thing must never $action")
print(template.substitute(thing='man', action='show his shocks'))
values={}
values['thing'] = 'woman'
values['action'] = 'tell secrets'
print(template.substitute(values))