__author__ = 'Son-Huy'
__version__ = 0.1

roll_width = 140
price_per_metre = 5

window_height = input('Enter the height of the window (cm): ')
window_width = input('Enter the width of the window (cm): ')

curtain_height = float(window_height) + 15
curtain_width = float(window_width) * 0.75 + 20

widths = curtain_width / roll_width
total_length = curtain_height * widths

total_length = total_length * 2 / 10

price = total_length * price_per_metre

print('You need', "{0:.2f}".format(total_length), "metres of cloth for", "{0:.2f}".format(price), "$")