__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from math import sqrt


def solve_quadratic_equation(a: int, b: int, c: int) -> tuple:
    delta = b * b - 4 * a * c
    a2 = a * 2

    if delta >= 0:
        sqrt_delta = int(sqrt(delta))
        return ((-b + sqrt_delta) // a2, (-b - sqrt_delta) // a2)
    else:
        x0_format, x1_format = '%d+%di', '%d-%di'
        sqrt_delta = int(sqrt(-delta))
        x, y = -b // a2, sqrt_delta // a2
        return (x0_format % (x, y), x1_format % (x, y))


def solve_quadratic_equation_input() -> tuple:
    (a, b, c) = map(int, input().split())
    return solve_quadratic_equation(a, b, c)


def solve_quadratic_equation_input_to_string() -> str:
    return ' '.join(str(i) for i in solve_quadratic_equation_input())


def main() -> int:
    n = int(input())
    results = '; '.join(solve_quadratic_equation_input_to_string()
                        for _ in range(n))

    print(results)
    return 0


if __name__ == '__main__':
    exit(main())