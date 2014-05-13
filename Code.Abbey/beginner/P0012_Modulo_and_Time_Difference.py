__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def time_to_int(timestamp: tuple) -> int:
    return timestamp[3] + timestamp[2] * 60 + timestamp[1] * 3600 + timestamp[0] * 86400


def int_to_time(times_int: int) -> tuple:
    days = times_int // 86400
    times_int %= 86400

    hours = times_int // 3600
    times_int %= 3600

    minutes = times_int // 60
    times_int %= 60

    seconds = times_int

    return (days, hours, minutes, seconds)


def time_to_string(timestamp: tuple) -> str:
    return '(%d %d %d %d)' % (timestamp[0], timestamp[1], timestamp[2], timestamp[3])


def input_timestamp() -> list:
    (d1, h1, m1, s1, d2, h2, m2, s2) = map(int, input().split())
    return [(d1, h1, m1, s1), (d2, h2, m2, s2)]


def timestamp_difference(timestamps: list) -> tuple:
    timestamp0 = time_to_int(timestamps[0])
    timestamp1 = time_to_int(timestamps[1])
    difference_int = timestamp1 - timestamp0
    difference_time = int_to_time(difference_int)

    return difference_time


def main() -> int:
    n = int(input())
    results = [time_to_string(timestamp_difference(input_timestamp())) for _ in range(n)]

    print(' '.join(results))


if __name__ == '__main__':
    exit(main())