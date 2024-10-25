my_dict = {'Andrey':1999, 'Pavel':2001, 'Alina':1998}
print(my_dict)
print(my_dict['Andrey'])
my_dict['Danya']=2004
print(my_dict['Danya'])
del my_dict['Alina']
print(my_dict.get('Alina'))
print(my_dict)


my_set = {2, 'Banana', 256.1, 2, 'Banana'}
print(my_set)
my_set.add('Pineapple')
my_set.add(3)
my_set.discard(2)
print(my_set)