__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def decrypt(message: str, k: int) -> str:
    char_list = list(message)
    min_ord, max_ord = ord('A'), ord('Z')

    for i in range(len(message) - 1):
        ordinal = ord(char_list[i])

        if ordinal < min_ord or ordinal > max_ord:
            continue

        ordinal -= k

        if ordinal < min_ord:
            ordinal += 26

        char_list[i] = chr(ordinal)

    return ''.join(char_list)


def decrypt_input(k: int) -> str:
    return decrypt(input(), k)


def main() -> int:
    (n, k) = map(int, input().split())
    results = [decrypt_input(k) for _ in range(n)]

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())