__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/fahrenheit-celsius'
__version__ = '1.0'

fahrenheits = [int(word) for word in input().split()]
celsiuses = [str(round((fahrenheit - 32) / 1.8)) for fahrenheit in fahrenheits[1:]]
print(' '.join(celsiuses))