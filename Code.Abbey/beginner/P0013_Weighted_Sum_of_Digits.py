__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/weighted-sum-of-digits'
__version__ = '1.0'


def wsd(number: str) -> int:
    weighted_sum = 0

    for i in range(len(number)):
        weighted_sum += int(number[i]) * (i + 1)

    return weighted_sum


def main() -> int:
    n = int(input())
    results = [''] * n
    inputs = input().split()

    for i in range(n):
        results[i] = str(wsd(inputs[i]))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())