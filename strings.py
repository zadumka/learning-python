print('hello my friend')
#String Indexing
# У Python ми використовуємо дужки [] після об'єкта, щоб викликати його індекс.
# Слід також зазначити, що індексація починається з 0 для Python.
s = ('he', 'she', 'it', 'we', 'they', 'are')
print(s[0])
print(s[2])
print(s[-1])

# We can use a : to perform slicing which grabs everything up to a designated point. For example:

mystring = ('abcdefgeijklmnop')

#вся строка на включаючи перший значення
print(mystring[1:])
# вся строка без перших трьох
print(mystring[3:])
#перше значення строки
print(mystring[:1])
# перших три
print(mystring[:3])
# весь рядок
print(mystring[:])
#весь рядок без останнього значення
print(mystring[:-1])
# весь рядок. Захопити все, але йти в кроках розміром 1
print(mystring[::1])
#варізка через одне значення. Захопити все, але йти в кроках розміром 2
print(mystring[::2])
# перевертає рядок задом на перед
print(mystring[::-1])

# Важливо відзначити, що рядки мають важливу властивість, відому як незмінність.
#Це означає, що після створення рядка елементи всередині нього не можуть бути змінені або замінені.
# Наприклад:
#print(s('Hello'))
#print(s[0] == 'S')

#Concatenate strings! (Cклеювання рядків)
my_string = ('Hello')
my_new_string = my_string + ' my friend'
print(my_new_string)

#Форматування друку
#Ми можемо використовувати метод .format(), щоб додати відформатовані об’єкти до надрукованих рядкових операторів.
#Найпростіший спосіб показати це на прикладі:

print('Insert another string with curly brackets: {}'.format('The inserted string'))
# Concatenate strings! (Cклеювання рядків)
#Один з найбільш поширених методів - використання функції format().
# Для цього ви можете створити рядок з місцем для вставки значень,
# використовуючи фігурні дужки {} як заповнювачі, і потім передавати
# ці значення як аргументи у функцію format(). Ось приклад:

name = "John"
age = 30
print("My name is {} and I'm {} years old".format(name, age))

player = 'Thomas'
points = 33
print('Last night, '+player+' scored '+str(points)+' points.')
#string formatting
print(f'Last night, {player} scored {points} points.')

#У Python 3.6 і вище можна використовувати так званий f-рядок (f-string),
# який дозволяє вставляти змінні без використання функції format().
# Для створення f-рядка необхідно перед рядком поставити букву "f"
name = "John"
age = 30
print(f"My name is {name} and I'm {age} years old")

