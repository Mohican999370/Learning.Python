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
    for i in range(0, 11):
        for j in range(1, 6):
            if (is_multiple(i, j)):
                print(i, " is multiple of ", j);
            else:
                print(i, " is NOT multiple of ", j);