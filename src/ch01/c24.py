'''
Created on 6 août 2013

@author: Son-Huy TRAN
'''

if __name__ == '__main__':
    vowels = "aeiou";
    input_string = input("Enter a string: ");
    
    result = sum(k in vowels for k in input_string);
    print(result);