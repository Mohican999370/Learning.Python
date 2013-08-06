# -*- coding: utf-8 -*-
'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''
from itertools import permutations;

if __name__ == '__main__':
    perms = permutations(['c', 'a', 't', 'd', 'o', 'g']);
    
    for p in perms:
        print(''.join(p));