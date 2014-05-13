__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def generate_prime_number(max_number: int) -> list:
    primes = [2]

    for number in range(3, max_number + 1, 2):
        i = 0
        current = primes[i]

        while current * current < number and number % current != 0:
            i += 1
            current = primes[i]

        if number % current != 0:
            primes.append(number)

    return primes


def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)

    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def main() -> int:
    primes = [0] + primes1(2800000)
    n = int(input())
    data = [int(word) for word in input().split()]
    result = [str(primes[i]) for i in data]

    print(' '.join(result))
    return 0


if __name__ == '__main__':
    exit(main())