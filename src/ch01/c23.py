'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''
from ch01 import read_array;

if __name__ == '__main__':
    a_list = read_array();
    index = input("What is the position of the element whose value you want to change? ");
    value = input("And you want change to which value? ");
    
    try:
        a_list[index] = value;
    except:
        print("Don’t try buffer overflow attacks in Python!");