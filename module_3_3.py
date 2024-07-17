def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params('Hello', 5, False)
print_params(25)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [True, 1, 'Hi']
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*value_list)
print_params(**values_dict)
values_list_2 = [2, True]
print_params(*values_list_2, 42)

