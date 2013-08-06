# -*- coding: utf-8 -*-
'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''

if __name__ == '__main__':
    try:
        a = int(input("Enter number a : "));
        b = int(input("Enter number b : "));
        c = int(input("Enter number c : "));
        
        if(a + b == c):
            print("a + b = c");
        elif(a == b - c):
            print("a = b - c");
        elif(a * b == c):
            print("a * b = c");
        else:
            print("a, b, c can not be used");
    except Exception as e:
        print("Invalid input");