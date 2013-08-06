# -*- coding: utf-8 -*-
'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''
from math import pow;

def sh_norm(v, p = 2):
    try:
        sh_sum = sum([pow(k, p) for k in v]);
        return pow(sh_sum, 1.0 / p);
    except Exception as ex:
        print(ex);
        return None;

if __name__ == '__main__':
    v = [4, 3];
    p = 2;
    print(sh_norm(v, p));
    print(sh_norm(v));