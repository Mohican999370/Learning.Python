__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def x_me(n: int, inputs: list) -> bool:
    n_minus_1 = n - 1
    first_char = inputs[0][0]
    second_char = inputs[0][1]

    if first_char == second_char:
        return False

    for i in range(n):
        for j in range(n):
            if i == j or i + j == n_minus_1:
                if inputs[i][j] != first_char:
                    return False
            else:
                if inputs[i][j] != second_char:
                    return False

    return True


def main() -> int:
    n = int(input())
    inputs = []

    for _ in range(n):
        inputs.append(input())

    print('YES' if x_me(n, inputs) else 'NO')
    return 0


if __name__ == '__main__':
    exit(main())