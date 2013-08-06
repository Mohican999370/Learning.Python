# -*- coding: utf-8 -*-
'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''
from math import log2;
from math import floor;

if __name__ == '__main__':
    n = int(input("Enter an integer n > 2: "));
    print("Must divide this number by 2:", floor(log2(n)), "TIMES");