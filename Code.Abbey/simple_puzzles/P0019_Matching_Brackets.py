__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def is_matched(value: str) -> bool:
    brackets_stack = []
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    for char in value:
        if char == '(' or char == '[' or char == '{' or char == '<':
            brackets_stack.append(char)
        elif char in brackets.keys():
            if len(brackets_stack) <= 0 \
                    or brackets_stack[-1] != brackets[char]:
                return False
            else:
                brackets_stack.pop()

    return len(brackets_stack) == 0


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        results[i] = '1' if is_matched(input()) else '0'

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())