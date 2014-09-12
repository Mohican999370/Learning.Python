__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)

    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def main() -> int:
    primes = primes1(1000001)
    tprimes = [i * i for i in primes]

    n = int(input())
    inputs = [int(word) for word in input().split()]
    messages = ['NO', 'YES']
    results = [messages[i in tprimes] for i in inputs]
    print('\n'.join(results))

    return 0


if __name__ == '__main__':
    exit(main())