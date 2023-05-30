#Вбудована функція len () Python підраховує всі символи рядка, включаючи пробіли та пунктуацію.
print(len('sum string has letters'))



#! *args and **kwargs

#? *args - це параметр функції в Python, який дозволяє передавати змінну кількість позиційних аргументів у функцію.
#? Коли ви визначаєте параметр зі зірочкою перед ним, наприклад *args, це означає, що функція може приймати будь-яку
#? кількість позиційних аргументів, і ці аргументи будуть зберігатись у вигляді кортежу args.
def myfunc(*args):
    return sum(args)* 0.05

print(myfunc(40,40))

#?**kwargs - це параметр функції в Python, який дозволяє передавати змінну кількість іменованих аргументів у функцію.
#? Коли ви визначаєте параметр зі зірочкою перед ним, наприклад **kwargs, це означає, що функція може приймати
#? будь-яку кількість іменованих аргументів, і ці аргументи будуть зберігатись у вигляді словника kwargs,
#? де ключами є імена аргументів, а значеннями - відповідні значення аргументів.
def myfunc1(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice {}'.format(kwargs['fruit']))
    else:
        print('I did not fiend eny fruit here')
myfunc1(windows='close', fruit='apple',)

def myfunc2(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc2(10,20,30,fruit = 'banana', food='apple', windows='close')

def myfunc(*args):
    return sum(args)
print(myfunc(1,2,3))

def myfunc(*args):
    list = []
    for num in args:
        if num % 2 == 0:
            list.append(num)
    return list
number = myfunc(3, 2, 5, 4, 7, 6)
print(number)
