__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())
    a = sorted([int(word) for word in input().split()])
    m = int(input())
    b = sorted([int(word) for word in input().split()], reverse=True)
    max_match = 0
    result = 0

    for i in range(n):
        for j in range(m):
            if b[j] % a[i] == 0:
                temp = b[j] // a[i]

                if temp > max_match:
                    max_match = temp
                    result = 1
                elif temp == max_match:
                    result += 1

                break

    print(result)
    return 0


if __name__ == '__main__':
    exit(main())