'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''

def is_even(k):
    try:
        return bool(not(k & 1));
    except:
        print("Invalid arguments");
        return False;

if __name__ == '__main__':
    for i in range(-5, 6):
        print(i, ":", "even" if (is_even(i)) else "NOT even");