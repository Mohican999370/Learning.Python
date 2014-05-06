__author__ = 'Son-Huy TRAN'

class Roulette:
    def __init__(self, devise):
        self.__devise = devise

    def get_devise(self):
        return self.__devise

    def set_devise(self, devise):
        self.__devise = devise

    def del_devise(self):
        del self.__devise

    devise = property(get_devise, set_devise, del_devise, 'La devise utilisée par le casino')