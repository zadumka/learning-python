# Basic Built-in String methods

#Ми називаємо методи з періодом, а потім назвою методу. Методи бувають у вигляді:

# object.method (параметри)
s = ('hello my best day')
print(s)

print(s.upper())

print(s.lower())

print(s.split())

# *Basic List Methods:

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

# Dictionary Methods
# clear(): видаляє всі елементи словника.
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.clear())
# copy(): повертає копію словника.
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.copy())
# fromkeys(seq, value): повертає словник, створений зі списку ключів seq, кожен з яких має значення value.
my_lists = ['one', 'two', 'three', 'six', 'ten', 'five', 'seven', 'six' ]
dict_lists = dict.fromkeys(my_lists, 0)
print(dict_lists)
# get(key, default=None): повертає значення ключа key, якщо він існує в словнику.
# Якщо ключ не існує, повертається значення за замовчуванням default (якщо воно встановлено).
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
ten = dict_lists.get('ten')
print(ten)
# items(): повертає список пар "ключ-значення" в словнику.
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
print(dict_lists.items())
# keys(): повертає список ключів у словнику.
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
print(dict_lists.keys())
# pop(key, default=None): видаляє ключ key зі словника і повертає його значення.
# Якщо ключ не знайдено, повертається значення за замовчуванням default (якщо воно встановлено).
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
delete_value = dict_lists.pop('six')
print(delete_value)
# popitem(): видаляє та повертає останню пару "ключ-значення" зі словника.
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
print(dict_lists.popitem())

# setdefault(key, default=None): повертає значення ключа key, якщо він існує в словнику.
# Якщо ключ не існує, додає його зі значенням default (якщо воно встановлено)
#і повертає значення за замовчуванням.
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
two_value = dict_lists.setdefault('two', 12)
print(two_value)

twelve = dict_lists.setdefault('twelve', 12)
print(twelve)
# update(other): додає пари "ключ-значення" з іншого словника other до поточного словника.
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
my_fruite = {'apple': 1, 'banana': 2, 'orange': 3}
dict_lists.update(my_fruite)
print(dict_lists)
# values(): повертає список значень у словнику.
dict_lists = {'one': 1, 'two': 2, 'three': 3, 'six': 6, 'ten': 10, 'five': 5, 'seven': 7}
print(dict_lists.values())


#Basic Tuple Methods

# index() - щоб ввести значення та повернути індекс
my_tupl = (1, 3, 5, 'seven', 5, 3)
print(my_tupl.index('seven'))

# count() - щоб підрахувати кількість разів появи значення
my_tupl = (1, 3, 5, 'seven', 5, 3)
print(my_tupl.count(5))