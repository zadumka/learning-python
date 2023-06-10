#! Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4/3) * 3.14 * rad ** 3
print(vol(2))

#! Напишіть функцію, яка перевіряє, чи число знаходиться в заданому діапазоні (включно з нижньою та верхньою межами).

def ran_check(num,low,high):
    if num in range(low, high + 1):
        print('{} is in range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')


print(ran_check(10, 2, 7))

#! Write a Python function that accepts a string and calculates the number of
#! upper case letters and lower case letters.

def up_lov(s):
    uppercase_count = 0
    lowercase_count = 0

    for letter in s:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower():
            lowercase_count += 1

    return'Кількість великих літер:', uppercase_count, 'Кількість малих літер:', lowercase_count


print(up_lov('Hello Mr. Rogers, how are you this fine Tuesday?'))
