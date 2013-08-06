'''
Created on 6 août 2013

@author: Son-Huy
'''

if __name__ == '__main__':
    lines = list();
    
    try:
        while(True):
            lines.append(input());
    except Exception as e:
        for i in range(len(lines) - 1, -1, -1):
            print(lines[i]);