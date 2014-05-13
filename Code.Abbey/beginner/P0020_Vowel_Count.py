__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/vowel-count'
__version__ = '1.0'

n = int(input())
vowels = 'aeiouy'
results = [''] * n

for i in range(n):
    count = {}
    value = input()

    for vowel in vowels:
        count[vowel] = value.count(vowel)

    results[i] = str(sum(count.values()))

print(' '.join(results))