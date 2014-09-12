__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    g = [None] * 5
    gsum = [None] * 5

    for i in range(5):
        g[i] = [int(word) for word in input().split()]
        gsum[i] = [0] * 5

    for i in range(5):
        for j in range(5):
            gsum[i][j] = g[i][j] + g[j][i]

    max_row_2_values = -1
    max_row_2_values_index = -1

    for i in range(5):
        temp = sorted(gsum[i])
        values_2 = temp[3] + temp[4]

        if values_2 > max_row_2_values:
            max_row_2_values = values_2
            max_row_2_values_index = i

    result = max_row_2_values * 2



    print(gsum)

    return 0


if __name__ == '__main__':
    exit(main())