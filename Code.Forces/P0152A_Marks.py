__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (n, m) = map(int, input().split())
    students = [''] * n
    max_marks = ['0'] * m

    for i in range(n):
        marks = input()
        students[i] = marks

        for j in range(m):
            if marks[j] > max_marks[j]:
                max_marks[j] = marks[j]

    count_successful = 0

    for i in range(n):
        is_successful = False

        for j in range(m):
            if students[i][j] == max_marks[j]:
                is_successful = True

        if is_successful:
            count_successful += 1

    print(count_successful)
    return 0


if __name__ == '__main__':
    exit(main())