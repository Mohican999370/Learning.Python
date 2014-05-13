__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/body-mass-index'
__version__ = '1.0'

LOWER = 'lower'
UPPER = 'upper'
LABEL = 'label'

indexes = [
    {
        LOWER: 0.0,
        UPPER: 18.5,
        LABEL: 'under'
    }, {
        LOWER: 18.5,
        UPPER: 25.0,
        LABEL: 'normal'
    }, {
        LOWER: 25.0,
        UPPER: 30.0,
        LABEL: 'over'
    }, {
        LOWER: 30.0,
        UPPER: 1000000.0,
        LABEL: 'obese'
    }
]


def get_index(weight: float, height: float) -> str:
    value = weight / (height * height)

    for indexi in indexes:
        if value >= indexi[LOWER] and value < indexi[UPPER]:
            return indexi[LABEL]

    return 'unknown'


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (weight, height) = map(float, input().split())
        results[i] = get_index(weight, height)

    print(' '.join(results))

    return 0


if __name__ == '__main__':
    exit(main())