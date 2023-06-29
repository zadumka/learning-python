#*  Умовні оператори if, elif, else

a = 8
b = 5
if a < b:
    print('значення а менше за b')
else:
    print('значення а більше за b')

print('поза межами блоку if')

c = 9
d = 9
if c < d:
    print('значення с менше d')
elif c == d:
    print('значення c дорівнює d')
else:
    print('значення c більше d')

g = 8
f = 7
if g < f:
    print('значення g менше f')
else:
    if g == f:
        print('значення g дорівнює f')
    else:
        print('значення g більше f')

name = 'Tom'
height = 1.73
weight = 65

bmi = weight/(height ** 2)
print('Індекс маси тіла: {:.2f}'.format(bmi))
print('Індекс маси тіла: {:.3f}'.format(bmi))
if bmi < 18:
    print('У ' + name + ' не достатня вага. Вам потрібно краще харчуватись')
elif bmi < 25:
    print('У ' + name + ' нема зайвої ваги')
elif bmi == 25:
    print('У ' + name + ' ідеальна вага')
else:
    print('У ' + name + ' зайва вага')

#? print('Індекс маси тіла: {:.1f}'.format(bmi))
#? Для виведення однієї цифри після десяткової крапки можна скористатись методом format і використати шаблон
#? форматування числа з плаваючою точкою з однією цифрою після крапки {:.1f}.
#? Також, можна замість використання методу str() для перетворення числа у рядок,
#? просто використати рядковий метод .format() для підстановки числа у рядок.

# ! Також можна використати f-рядки (f-strings) для досягнення того ж ефекту, як у попередньому прикладі.
# !  Ось як це можна зробити за допомогою f-рядка:
print(f'Індекс маси тіла: {bmi:.1f}')
if bmi < 18:
    print('У ' + name + ' не достатня вага. Вам потрібно краще харчуватись')
elif 18 <= bmi < 25:
    print('У ' + name + ' нема зайвої ваги')
elif bmi == 25:
    print('У ' + name + ' ідеальна вага')
else:
    print('У ' + name + ' зайва вага')
