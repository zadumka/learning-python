def function1():
    print('Hello world')


print('Hello from out')


def function1():
    print('Hello world')


function1()


def function2(x):
    return 2 * x


a = function2(10)
print(a)


def function3():
    return 5


print(function3())


def function4(x):
    print(x)
    print('Good day')
    return 3 * x


a = function4(10)
print(a)


# ! функції можуть мати аргумент але не мати вихідного значення

def function5(text):
    print(text)
    print('fhskdjhskdhskhsf')


print(function5(5))


# ! функції можуть не мати аргументу але мати вихідне значення

def function6():
    return 5


print(function6())

# ? Задача: Розрахувати індекс маси тіла через функцію

name1 = 'Tom'
height1 = 1.63
weight1 = 65

name2 = 'Alex'
height2 = 2
weight2 = 90

name3 = 'Max'
height3 = 1.75
weight3 = 110

def bmi_calculator(name, height, weight):
    bmi = weight/(height ** 2)
    print('Індекс маси тіла: {:.1f}'.format(bmi))
    if bmi < 18:
        return 'Індекс маси тіла: {:.1f}'.format(bmi) + 'У ' + name + ' не достатня вага. Вам потрібно краще харчуватись'
    elif bmi < 25:
        return 'У ' + name + ' нема зайвої ваги'
    elif bmi == 25:
        return 'У ' + name + ' ідеальна вага'
    else:
        return 'У ' + name + ' зайва вага'
bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)
print(bmi1)
print(bmi2)
print(bmi3)

# ? Задача: Конвертувати милі в кілометри

mile = 25

def convert_kilometrs(mile):
    km = mile * 1.60934
    return km


km = convert_kilometrs(mile)
print(km)

# ? Задача: Розрахувати площу прямокутника

b = 7
c = 5

def area(b,c):
    a = b * c
    return a

a = area(b,c)
print(a)

# ? Задача: вибрати парні числа

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(my_list):
    even_number = []
    for i in my_list:
        if i % 2 == 0:
            even_number.append(i)
    return even_number

even_number = is_even(my_list)
print(even_number)


