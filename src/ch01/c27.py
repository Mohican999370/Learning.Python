# -*- coding: utf-8 -*-
'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''
import math;

def factors(n):
    new_factors = list();
    k = 1;
    maxk = math.sqrt(n);
    
    while (k < maxk):
        if (n % k == 0):
            yield k;
            new_factors.insert(0, n // k);
        k += 1;
        
    if (k * k == n):
        yield k;
    
    for i in new_factors:
        yield i;
        
# generator that computes factors #whilek<sqrt(n)
# special case if n is perfect square

if __name__ == '__main__':
    for i in factors(100):
        print(i, end = " ");