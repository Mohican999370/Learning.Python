__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())
    n_minus_1 = n - 1
    homes = []
    aways = []
    results = []

    for i in range(n):
        (home, away) = map(int, input().split())
        homes.append(home)
        aways.append(away)
        results.append([n_minus_1, n_minus_1])

    for i in range(n):
        for j in range(i + 1, n):
            if homes[i] == aways[j]:
                results[j][0] += 1
                results[j][1] -= 1
            if homes[j] == aways[i]:
                results[i][0] += 1
                results[i][1] -= 1

    output = ['%d %d' % (results[i][0], results[i][1]) for i in range(n)]
    print('\n'.join(output))

    return 0


if __name__ == '__main__':
    exit(main())