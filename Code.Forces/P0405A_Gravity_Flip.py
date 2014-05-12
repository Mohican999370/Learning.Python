__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/405/A'
__version__ = '1.0'

input()
cubes = [int(i) for i in input().split()]
cubes = sorted(cubes)
output = [str(i) for i in cubes]

print(' '.join(output))