'''
Created on 6 août 2013

@author: Son-Huy
'''

def read_array():
    input_string = input("Enter the elements separated by spaces: ");
    tokens = input_string.split(" ");
    return [int(token) for token in tokens];

def dot_product(list_1, list_2):
    try:
        length = len(list_1);
        
        if (length != len(list_2)):
            raise ValueError("Two lists do not have the same length");
        
        return [list_1[k] * list_2[k] for k in range(length)];
    except Exception as e:
        print ("ERROR:", e);
        return None;

if __name__ == '__main__':
    list_1 = read_array();
    list_2 = read_array();
    
    print(dot_product(list_1, list_2));
    