__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/158/C'
__version__ = '1.0'

pwd = 'pwd'

n = int(input())
commands = [''] * n

for i in range(n):
    commands[i] = input()

path = ['']

for i in range(n):
    command = commands[i]

    if (command == pwd):
        print('/'.join(path) + '/')
    else:
        path_to_go = command[3:]
        dirs = []

        if (path_to_go[0] == '/'):
            path = ['']
            dirs = path_to_go.split('/')[1:]
        else:
            dirs = path_to_go.split('/')

        for dir in dirs:
            if dir == '..':
                if len(path) > 1:
                    path.pop()
            else:
                path.append(dir)