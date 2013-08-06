# -*- coding: utf-8 -*-
'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''


def sh_make_change(charged, given, monetary_system):
    if (given <= charged):
        return None;
    
    sum_return = given - charged;
    money_return = list();
    
    for i in range(len(monetary_system)):
        money_return.append(sum_return // monetary_system[i]);
        sum_return = sum_return % monetary_system[i];
    
    return money_return;

if __name__ == '__main__':
    charged = int(input("Charged? "));
    given = int(input("Given? "));
    monetary_system = [500, 200, 100, 50, 20, 10, 5, 2, 1];
    remainder = sh_make_change(charged, given, monetary_system);
    
    for i in range(len(remainder)):
        if (remainder[i] > 0):
            print(remainder[i], ' * ', monetary_system[i], '$', sep='');