'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''

def minmax(alist):
    try:
        if (not(alist)):
            raise ValueError("Invalid argument (possible empty list)");
        
        currentmin = alist[0];
        currentmax = alist[1];
        
        for i in range(1, len(alist)):
            if (alist[i] > currentmax):
                currentmax = alist[i];
            if (alist[i] < currentmin):
                currentmin = alist[i];
                
        return currentmin, currentmax;
    except Exception as e:
        print(e);
        return;

if __name__ == '__main__':
    print(minmax([3, 7, 5, 1, 2, 4]));