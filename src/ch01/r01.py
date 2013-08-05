'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''

def is_multiple(n, m):
    try:
        return n % m == 0;
    except:
        return False;

if __name__ == '__main__':
    print(is_multiple(10, 5));
    print(is_multiple(0, 5));
    print(is_multiple(10, 3));
    print(is_multiple(10, 0));