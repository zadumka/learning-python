#* Functions and Methods Homework


#! Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4 / 3) * 3.14 * rad ** 3


print(vol(2))


# ! Напишіть функцію, яка перевіряє, чи число знаходиться в заданому діапазоні (включно з нижньою та верхньою межами).

def ran_check(num, low, high):
    if num in range(low, high + 1):
        print('{} is in range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')


print(ran_check(3, 2, 7))


# ! Write a Python function that accepts a string and calculates the number of
# ! upper case letters and lower case letters.

def up_lov(s):
    uppercase_count = 0
    lowercase_count = 0

    for letter in s:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower():
            lowercase_count += 1

    return 'Кількість великих літер: {}'.format(uppercase_count), 'Кількість малих літер: {}'.format(lowercase_count)


print(up_lov('Hello Mr. Rogers, how are you this Fine Tuesday?'))


# ! Напишіть функцію Python, яка приймає список і повертає новий список з унікальними елементами першого списку.
# ! Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]

def get_unique_number(number_list):
    unique_number = set(number_list)
    return list(unique_number)


print(get_unique_number([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7]))


#! Напишіть функцію Python для множення всіх чисел у списку.
#! Sample List : [1, 2, 3, -4]

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply([1, 2, 3, -4, 2]))


#* Function Practice Exercises

# ! МЕНШЕ З ДВОХ ПАРНИХ: Напишіть функцію, яка повертає менше з двох заданих чисел,
# ! якщо обидва числа парні, але повертає більше, якщо одне чи обидва числа непарні.
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(4, 8))

# ! ANIMAL CRACKERS: Напишіть, що функція приймає рядок із двох слів і повертає True,
# ! якщо обидва слова починаються з однієї літери

def animal_crackers(text):
    wirdlist = text.split()
    # функція перевіряє, чи є перша літера першого слова (знаходиться у wirdlist[0][0])
    # рівною першій літері другого слова (знаходиться у wirdlist[1][0]).
    return wirdlist[0][0] == wirdlist[1][0]


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy kangaroo'))

# ! задано два цілі числа, повертає True, якщо сума цілих чисел дорівнює 20 або
# ! якщо одне з цілих чисел дорівнює 20. Якщо ні, повертає False

def makes_twenty(n1, n2):
    if (n1 + n2) == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 0))
print(makes_twenty(10, 11))
print(makes_twenty(0, 20))


#? LEVEL 1 PROBLEMS

# ! СТАРИЙ МАКДОНАЛЬД: Напишіть функцію, яка робить першу та четверту літери імені великими

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    # name[:3].capitalize() - цей вираз вибирає перші три символи рядка name
    # за допомогою синтаксису зрізу (name[:3]), а потім застосовує до них метод .capitalize(),
    # щоб перетворити їх на великі літери.
    # name[3:].capitalize() - цей вираз вибирає всі символи рядка name починаючи
    # з індексу 3 і до кінця рядка (name[3:]), а потім застосовує до них метод .capitalize(),
    # щоб перетворити їх на великі літери.
    else:
        return 'Name is too short!'


print(old_macdonald('macdonald'))


# !MASTER YODA: Дано речення, поверніть речення зі словами, перевернутими
# ! master_yoda('I am home') --> 'home am I'
# ! master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda('home am I'))
print(master_yoda('ready are We'))

#! ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(almost_there(90))
#--> True
print(almost_there(104))
#--> True
print(almost_there(150))
#--> False
print(almost_there(209))
#--> True

#? LEVEL 2 PROBLEMS

# !Маючи список int, поверніть True, якщо масив десь містить 3 поруч із 3.

def find3(nums):
    for n in range(0, len(nums) - 1):
        if nums[n] == 3 and nums[n + 1] == 3:
            return True

    return False


print(find3([1, 3, 3, 2, 3]))
print(find3([1, 3, 1, 3]))

#! PAPER DOLL: Given a string, return a string where for every character
#! in the original there are three characters

#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def return_character(paper_doll):
    result = ''
    for letter in paper_doll:
        result += letter*3
    return result


print(return_character('Hello'))
print(return_character('Mississippi'))

# ! БЛЕКДЖЕК: Дано три цілі числа від 1 до 11, якщо їх сума менша або дорівнює 21, поверніть їх суму.
# ! Якщо їх сума перевищує 21 і є одинадцять, зменшіть загальну суму на 10.
# ! Нарешті, якщо сума (навіть після коригування) перевищує 21, поверніть «the sum more then 21»

def blackjack(a, b, c):
    if (a + b + c) <= 21:
        return a + b + c
    elif (a + b + c) <= 31 and 11 in (a, b, c):
        return (a + b + c) - 10
    else:
        return 'the sum more then 21'


print(blackjack(9, 9, 10))
print(blackjack(5, 6, 7))
#--> 18

print(blackjack(9, 9, 9))
#--> 'the sum more then 21'

print(blackjack(9, 9, 11))
#--> 19

# ! SUMMER OF '69:Повернути суму чисел у масиві, ігноруючи відрізки чисел,
# ! які починаються з 6 і продовжуються до наступної 9 (кожне число 6 буде наступати принаймні одне число 9).
# ! Повернути 0, якщо немає жодних чисел.




#! Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only spring the words that start with s in this sentence scrole'

for word in st.split():
    if word[0] == 's':
        print(word)
# ! Use range() to print all the even numbers from 0 to 10.
for i in range(0, 11, 2):
    print(i)

# ! Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mylist = [num for num in range(1, 50) if num % 3 == 0]
print(mylist)

# ! Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word + " <-- has an even length!")

# ! Write a program that prints the integers from 1 to 100.
# ! But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# !For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

# ! Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
word_let = [word[0] for word in st.split()]
print(word_let)
