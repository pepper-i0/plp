my_list = []
my_list.append('10')
my_list.append('20')
my_list.append('30')
my_list.append('40')
print(my_list)

my_list[1] = '15'
print(my_list)

my_lists = ['50', '60', '70']

my_list.extend(my_lists)
print(my_list)

del my_list[-1]
print(my_list)

my_list.sort()
print(my_list)

print(my_list.index('30'))  
