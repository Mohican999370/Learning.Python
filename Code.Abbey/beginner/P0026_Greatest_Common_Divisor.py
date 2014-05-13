__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def gcd(number1: int, number2: int) -> int:
    if number2 == 0:
        return number1
    else:
        return gcd(number2, number1 % number2)


def gcd_lcm(number1: int, number2: int) -> tuple:
    gcd_result = gcd(number1, number2)
    return (gcd_result, number1 * number2 // gcd_result)


def gcd_lcm_to_string(number1: int, number2: int) -> str:
    gcd_lcm_result = gcd_lcm(number1, number2)
    return '(%d %d)' % gcd_lcm_result


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (a, b) = map(int, input().split())
        results[i] = gcd_lcm_to_string(a, b)

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())