'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''

def sh_list_reverse(alist):
    try:
        length = len(alist);
        
        if (length < 2):
            return;
        
        for i in range(length // 2):
            alist[i], alist[length - 1 - i] \
                = alist[length - 1 - i], alist[i]; 
        
        return;
    except Exception as e:
        print(e);
        return;

if __name__ == '__main__':
    alist = [1, 3, 5, 7, 9];
    blist = [1, 3, 5, 7, 9];
    sh_list_reverse(alist);
    blist.reverse()
    
    print(alist);
    print(blist);
    print(alist == blist);