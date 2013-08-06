'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''
def is_odd(number):
    try:
        return bool(number & 1);
    except Exception as ex:
        print(ex);
        return False;

def odd_product(a_list):
    try:
        length = len(a_list);
        
        if (length < 2):
            return None;
        
        for i in range(0, length - 1, 1):
            for j in range(i + 1, length, 1):
                if (is_odd(a_list[i]) and is_odd(a_list[j])):
                    return a_list[i], a_list[j];
        
        return None;
    except Exception as ex:
        print(ex);
        return None;

if __name__ == '__main__':
    a_list = [3, 2, 9, 7, 6, 4, 10];
    b_list = [2, 4, 6, 8];
    c_list = [3];
    d_list = list();
    
    print(odd_product(a_list));
    print(odd_product(b_list));
    print(odd_product(c_list));
    print(odd_product(d_list));