__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (sh, sm) = map(int, input().split(':'))
    (th, tm) = map(int, input().split(':'))

    if sh < th or (sh == th and sm < tm):
        sh += 24

    if sm < tm:
        sm += 60
        sh -= 1

    sm -= tm
    sh -= th

    print('%02d:%02d' % (sh, sm))

    return 0


if __name__ == '__main__':
    exit(main())