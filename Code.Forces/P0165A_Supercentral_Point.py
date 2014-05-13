__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/165/A'
__version__ = '1.0'

x, y = 'x', 'y'


def main() -> int:
    n = int(input())
    points = [None] * n

    for i in range(n):
        points[i] = {}
        xi, yi = map(int, input().split())
        points[i][x] = xi
        points[i][y] = yi

    left = [0] * n
    right = [0] * n
    upper = [0] * n
    lower = [0] * n

    for i in range(n - 1):
        for j in range(n):
            if (i == j):
                continue

            if points[i][x] == points[j][x]:
                if points[i][y] > points[j][y]:
                    lower[i] += 1
                    upper[j] += 1
                else:
                    lower[j] += 1
                    upper[i] += 1
            elif points[i][y] == points[j][y]:
                if points[i][x] > points[j][x]:
                    left[i] += 1
                    right[j] += 1
                else:
                    left[j] += 1
                    right[i] += 1

    count = 0

    for i in range(n):
        if left[i] and right[i] and upper[i] and lower[i]:
            count += 1

    print(count)

    return 0


if __name__ == '__main__':
    main()