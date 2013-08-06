'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''

def are_all_distinct(a_list):
    try:
        length = len(a_list);
        
        for i in range(length - 1):
            for j in range(i + 1, length):
                if (a_list[i] == a_list[j]):
                    return False;
                
        return True;
    except Exception as e:
        print(e);
        return False;

if __name__ == '__main__':
    a_list = [3, 1, 2, 4, 5, 9, 3, 6];
    b_list = [3, 1, 4, 5, 9, 8, 7];
    
    print(are_all_distinct(a_list));
    print(are_all_distinct(b_list));