'''
Created on 5 août 2013

@author: Son-Huy TRAN
'''
import random;

def sh_shuffle(a_list):
    try:
        # Creates a new list to store the result
        result = list();
        
        while len(a_list):
            # Randomizes an element in the list remaining
            index = random.randint(0, len(a_list) - 1);
            result.append(a_list[index]);
            
            # Remove this element from the list
            a_list.pop(index);
        
        # Re-adds the shuffled list
        a_list.extend(result);
    except Exception as ex:
        print(ex);
        return;

if __name__ == '__main__':
    a_list = [k for k in range(20)];
    sh_shuffle(a_list);
    
    print(a_list);