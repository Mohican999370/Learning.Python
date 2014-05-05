__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = ''
__version__ = '1.0'

my_list = [1, 2, 3]
print('before:', my_list)

my_list.append(4)
my_list.append(1)
print('after appending:', my_list)
print('occurrences of 1:', my_list.count(1))

my_list.extend([5, 6, 7])
print('after extending:', my_list)

my_list = my_list + [8, 9]
print('after extending:', my_list)

my_list[len(my_list):] = [10]
print('after extending:', my_list)

print('index of 1:', my_list.index(1))
# print('index of 11:', my_list.index(11)) # Exception

if (11 in my_list):
    print('index of 11:', my_list.index(11))
else:
    print('11 not found in the list')

my_list.insert(5, 'two')
print('after inserting:', my_list)

my_list.insert(len(my_list), 'eleven')
print('after inserting:', my_list)

print('popped element:', my_list.pop())
print('after popping:', my_list)

print('popped element:', my_list.pop(4))
print('after popping:', my_list)

my_list.remove('two')
print('after removing:', my_list)

my_list.reverse()
print('after reversing:', my_list)

new_list = my_list[:]
new_list.sort()
print('Sorted list:', new_list)

new_list.sort(reverse=True)
print('Reversely sorted list:', new_list)