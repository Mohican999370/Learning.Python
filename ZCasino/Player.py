__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

class Player:
    def __init__(self, name='New Player', budget=0):
        self.__name = name
        self.__budget = budget

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def del_name(self):
        del self.__name

    name = property(get_name, set_name, del_name, 'Player\'s name')

    def get_budget(self):
        return self.__budget

    def set_budget(self, value):
        self.__budget = value

    def add_to_budget(self, value):
        self.__budget += value

    def take_from_budget(self, value):
        if (value > self.__budget):
            return 0
        else:
            self.__budget -= value
            return value

    def del_budget(self):
        del self.__budget

    budget = property(get_budget, set_budget, del_budget, 'Player\'s budget')