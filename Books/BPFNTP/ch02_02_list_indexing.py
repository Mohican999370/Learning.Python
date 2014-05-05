__author__ = 'Son-Huy TRAN'
__spec__ = 'Print out a date, given year, month, and day as numbers'
__version__ = '1.0'

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

endings = ['st', 'nd', 'rd'] \
          + 17 * ['th'] \
          + ['st', 'nd', 'rd'] \
          + 7 * ['th'] \
          + ['st']

year = input('Year: ')
month = int(input('Month(1-12): '))
day = int(input('Day(1-31): '))

month_name = months[month - 1]
ordinal = repr(day) + endings[day - 1]

print(month_name, ' ', ordinal, ', ', year, sep='')