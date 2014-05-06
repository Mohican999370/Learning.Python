__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

import random


class Roulette:
    def __init__(self, max_number=50):
        self.__max_number = max_number

    def get_max_number(self):
        return self.__max_number

    def set_max_number(self, value):
        self.__max_number = value

    def del_max_number(self):
        del self.__max_number

    max_number = property(get_max_number, set_max_number, del_max_number, 'The number of numbers in the roulette')

    def next_number(self):
        value = random.randrange(self.__max_number)
        print('The roulette has stopped at', value)
        return value