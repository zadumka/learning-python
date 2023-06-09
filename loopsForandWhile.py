# ! Цикл while используется для выполнения блока кода до тех пор, пока выполняется некоторое условие.
# ! Таким образом, цикл while применяется, когда количество итераций неизвестно заранее, и зависит от того,
# ! когда будет выполнено определенное условие.
#
# ? С другой стороны, цикл for используется для перебора элементов в последовательности (например, в списке, кортеже или строке),
# ? и выполняет блок кода для каждого элемента в последовательности. Таким образом, цикл for применяется,
#? когда количество итераций известно заранее, и зависит от размера последовательности.

# Как правило, если вы знаете количество итераций, которые вам нужно выполнить, лучше использовать цикл for.
# Если количество итераций неизвестно заранее и зависит от выполнения условия, лучше использовать цикл while.
# Однако не забывайте, что цикл while может привести к бесконечному циклу, если условие никогда не станет ложным,
# так что используйте его с осторожностью.

my_list = [4, 6, 7, 9, 10, 12, -5, -10, -15]

# заводим переменную акумулятор(в єтой переменной будем считать сумму)
total = 0
# заводим переменную счетчик
i = 0
while my_list[i] > 0:
    total += my_list[i]
# инкрементируем переменную счетчик
    i += 1
#? також можна вирішити черещ цикл for, але сам цикл буде тривати довше, так як буде перебирати всі значення, які є в списку.
#? А цикл while дійде до першого відємного числа і закінче перебірку.
total1 = 0
for element in my_list:
    if element > 0:
        total1 += element
# Щоб скоротити час циклу for можна записати по іншому.
total2 = 0
for element in my_list:
#задаємо умову, якщо елемент <= 0 перериваємо перебірку елементів
    if element <= 0:
        break
    total2 += element

#print(total2)
#print(total1)
#print(total)

# ! Задача: Знайти сумму відємних чисел (двома способами, через цикл for, while)
my_list1 = [4, 6, 7, 9, 10, 12, -5, -10, -15, -18]

# ? цикл while
total3 = 0
i2 = 0
while i2 <len(my_list1):
    if my_list1[i2] < 0:
        total3 += my_list1[i2]
    i2 += 1
#print(total3)

# ? цикл for
total4 = 0
for i3 in my_list1:
    if i3 < 0:

        total4 += i3
#print(total4)

#! Задача: Вивести всі слова зі списки до ключового слова

my_list2 = ['Понеділок', 'Вівторок', 'Середа', 'Stop', 'Четверг', 'Субота']

for element in my_list2:
    if element == 'Stop':
        break
#    print(element)

#------------------------
names = ['Alex', 'Nik', 'Tom', 'Mike']

for i in range(len(names)):
    for j in range(i+1):
        print(names[i])



a = (10**2 / 2) + (25 * 2) + 0.25
print(a)

r=(5**2 * 4 / 2) + 50 + 0.25
print(r)

o = 3 + 1.5 + 4
print(o)
print(type(o))

s = 'hello'
print(s[1])

st='hello'
d = st[::-1]
print(d)

w = 'hello'
q = w + 'o'
print(q)

new_list1=[0,0,0]
print(new_list1)

new_list2=[0]*3
print(new_list2)

list3 = [1,2,[3,4,'hello']]
list3[2][2]='good bye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d2 = {'simple_key':'hello'}
print(d2['simple_key'])

d3 = {'k1':{'k2':'hello'}}
print(d3['k1']['k2'])

d4 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d4['k1'][0]['nest_key'][1][0])

d5 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d5['k1'][2]['k2'][1]['tough'][2][0])
