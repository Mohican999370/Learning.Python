__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

import math

from Roulette import Roulette
from Player import Player


class ZCasino:
    def __init__(self, currency='$'):
        self.__currency = currency
        self.__roulette = Roulette(50)
        self.__player = Player()

    def get_currency(self):
        return self.__currency

    def set_currency(self, value):
        self.__currency = value

    def del_currency(self):
        del self.__currency

    currency = property(get_currency, set_currency, del_currency, 'The currency used by ZCasino')

    def __welcome_player(self):
        self.__player.name = input('Welcome my dear player. May I know your name, please? ')
        self.__player.budget = int(input('How much money do you have? '))

    def __next_round(self):
        bet = -1

        while (bet < 0 or bet > self.__player.budget):
            try:
                bet = int(input(
                    'How much money do you want to place as bet? (Enter 0 to quit the game) (Your budget is %d) '
                    % self.__player.budget))
            except ValueError:
                print('You did not type a number. Please try again')
                bet = -1
                continue

            if (bet < 0):
                print('You cannot place a negative money amount. Please try again.')

            if (bet > self.__player.budget):
                print('You do not have enough money. Please try again.')

        bet = self.__player.take_from_budget(bet)

        if (bet > 0):
            player_number = -1

            while (player_number < 0 or player_number >= self.__roulette.max_number):
                try:
                    player_number = int(
                        input('What is the number you want to bet? (from 0 to %d) ' % (self.__roulette.max_number - 1)))
                except ValueError:
                    print('You didn\'t type a number. Please try again')
                    player_number = -1
                    continue

                if (player_number < 0):
                    print('You cannot bet a negative number. Please try again.')

                if (player_number >= self.__roulette.max_number):
                    print('This number is too big for the roulette. Please try again.')

            value = self.__roulette.next_number()
            winning_amount = 0

            if (value == player_number):
                winning_amount = bet * 4
                print('You chose the exact number. You gained', winning_amount, self.__currency)
            elif (value % 2 == player_number % 2):
                winning_amount = math.ceil(bet * 1.5)
                print('Your number and roulette number have the same color. You gained', winning_amount,
                      self.__currency)
            else:
                print('Sorry. You gained nothing. Please try again.')

            self.__player.add_to_budget(winning_amount)
            return True
        else:
            print('You chose to quit the game. Thank you and see you again.')
            return False

    def start(self):
        self.__welcome_player()

        while (self.__next_round()):
            pass

        return


if __name__ == "__main__":
    z_casino = ZCasino()
    z_casino.start()