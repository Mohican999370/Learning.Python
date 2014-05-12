__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/modular-calculator'
__version__ = '1.0'

current = int(input())

while True:
    command = input()
    operator = command[0]
    operand = int(command[2:])

    if operator == '+':
        current += operand
    elif operator == '*':
        current *= operand
    elif operator == '%':
        current %= operand
        break

print(current)