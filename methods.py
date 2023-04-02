# Basic Built-in String methods

#Ми називаємо методи з періодом, а потім назвою методу. Методи бувають у вигляді:

# object.method (параметри)
s = ('hello my best day')
print(s)

print(s.upper())

print(s.lower())

print(s.split())

# Basic List Methods

# append(item): Додає елемент item в кінець списку.
# extend(iterable): Додає елементи з ітерабельного об'єкту iterable (наприклад, іншого списку) в кінець списку.
# insert(index, item): Додає елемент item в список на позицію index.
# remove(item): Видаляє перше входження елемента item зі списку.
# Якщо елементу немає в списку, видає помилку ValueError.
# pop([index]): Видаляє та повертає елемент зі списку на позиції index.
# Якщо index не вказано, видаляє та повертає останній елемент списку.
# index(item): Повертає індекс першого входження елемента item в списку.
# Якщо елементу немає в списку, видає помилку ValueError.
# count(item): Повертає кількість входжень елемента item в списку.
# sort(): Сортує список в порядку зростання.
# reverse(): Перевертає порядок елементів у списку.

my_list = ['one', 'two','three']
my_list.append('four')
print(my_list)

my_list = ['one', 'two','three']
num_list = [ 4 , 5]
my_list.extend(num_list)
print(my_list)

my_list = ['one', 'two','three']
my_list.insert(2,"six")
print(my_list)

my_list = ['one', 'two','three']
my_list.remove('two')
print(my_list)

my_list = ['one', 'two','three']
my_list.pop(2)
print(my_list)

my_lists = ['one', 'two', 'three', 'six', 'ten', 'five', 'seven' ]
print(my_lists.index('three'))

my_lists = ['one', 'two', 'three', 'six', 'ten', 'five', 'seven', 'six' ]
print(my_lists.count('six'))

my_lists = ['one', 'two', 'three', 'six', 'ten', 'five', 'seven', 'six' ]
my_lists.sort()
print(my_lists)

my_lists = ['one', 'two', 'three', 'six', 'ten', 'five', 'seven', 'six' ]
my_lists.reverse()
print(my_lists)
