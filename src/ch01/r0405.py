'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''

def sum_squares(n):
    return sum([k * k for k in range(1, n)]);

if __name__ == '__main__':
    print(sum_squares(18));