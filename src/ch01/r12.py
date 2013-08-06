'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''
import random;

def sh_rand_choice(alist):
    try:
        index = random.randrange(start = 0, stop = len(alist), step = 1);
        return alist[index];
    except:
        return None;

if __name__ == '__main__':
    print(sh_rand_choice([1, 3, 5, 7, 9, 8, 6, 4, 2]));