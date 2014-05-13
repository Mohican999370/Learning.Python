__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())
    exercises = [int(word) for word in input().split()]
    total = [0] * 3

    for i in range(3):
        total[i] = sum(exercises[i::3])

    max_index = total.index(max(total))
    exercise_names = ['chest', 'biceps', 'back']

    print(exercise_names[max_index])

    return 0


if __name__ == '__main__':
    main()