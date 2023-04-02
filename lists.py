my_list = [123, 'hello', 345.45, 'today']
print(len(my_list))

# Indexing and Slicing (такеж саме, як і для рядків)
print(my_list[1])
print(my_list[1:])
print(my_list[::-1])
print(my_list[0:4:2])

# We can also use + to concatenate lists, just like we did for strings.
print(my_list + ['spring'])

my_list = my_list + ['bey']
print(my_list)

# Make the list double
print(my_list * 2)

# Nesting Lists (вкладеність списків)Ю Ми можемо вкладати декілька списків у один
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
big_list = [lst_1, lst_2, lst_3]
print(big_list)
print(big_list[1])

# ЗАДАЧКА
# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,3, [3,4,'hello']]
list3[3][2] = 'goodbey'
print(list3)

#List comprehensions - це спосіб створення списку в Python
#List comprehensions складається з виразу, який визначає значення кожного елемента нового списку,
# та одного або декількох циклів for, що вказують, звідки брати значення для виконання виразу.
mystring = 'Friday'
mylist = [letter for letter in mystring]
print(mylist)

my_list = [x for x in range(1, 11) if x % 2 == 0]
print(my_list)
# Створити новий список з двух інших списків перемноживши їх між собою
my_list1 = []

for x in [2, 4, 6]:
    for y in [10, 100, 1000]:
        my_list1.append(x * y)
print(my_list1)

## піднести до квадрату всі числа в списку
my_num = [x**2 for x in range(10)]
print(my_num)