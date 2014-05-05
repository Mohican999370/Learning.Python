__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

khathy_list = list('Kha-Thy NGO')
print('before:', khathy_list, '=', ''.join(khathy_list))
khathy_list[-1] = 'Ố'
print('after:', khathy_list, '=', ''.join(khathy_list))