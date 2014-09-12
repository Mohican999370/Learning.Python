__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    scales = input().split('|')
    remaining = input()
    sum_length = len(scales[0]) + len(scales[1]) + len(remaining)

    if sum_length % 2 != 0:
        print('Impossible')
    else:
        temp = sum_length // 2

        if len(scales[0]) > temp or len(scales[1]) > temp:
            print('Impossible')
        else:
            for i in range(2):
                remainingi = temp - len(scales[i])
                scales[i] += remaining[:remainingi]
                remaining = remaining[remainingi:]
            print(scales[0], scales[1], sep='|')

    return 0


if __name__ == '__main__':
    exit(main())