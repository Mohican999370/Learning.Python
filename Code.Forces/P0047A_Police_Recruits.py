__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def count_untreated_crimes(events: list) -> int:
    untreated = 0
    recruted = 0

    for event in events:
        if event > 0:
            recruted += event
        elif event == -1:
            if recruted <= 0:
                untreated += 1
            else:
                recruted -= 1

    return untreated


def main() -> int:
    input()
    events = [int(word) for word in input().split()]
    print(count_untreated_crimes(events))

    return 0


if __name__ == '__main__':
    exit(main())