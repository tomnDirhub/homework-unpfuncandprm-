def print_params(a = 1, b = 'ghost', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)        # Вызов работает но программа ругается на
print_params(c = [1, 2, 3]) # изменение типа данных параметров

print(sep='')

values_list = ['fake', False, 89]
values_dict = {'a': 72, 'b': 'cloud', 'c': True}
print_params(*values_list)
print_params(**values_dict)

print(sep='')

values_list2 = [False, 'joke']
print_params(*values_list2, 42)