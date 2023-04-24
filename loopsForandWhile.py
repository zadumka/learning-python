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

print(total2)
print(total1)
print(total)

