# -*- coding: utf-8 -*-
'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''

if __name__ == '__main__':
    input_string = input("Enter a sentence: ");
    print(''.join([k for k in input_string if k.isalpha() or k.isspace()]));