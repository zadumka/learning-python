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


# ! МЕНШЕ З ДВОХ ПАРНИХ: Напишіть функцію, яка повертає менше з двох заданих чисел,
# ! якщо обидва числа парні, але повертає більше, якщо одне чи обидва числа непарні.
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(4, 11))


# ! ANIMAL CRACKERS: Напишіть, що функція приймає рядок із двох слів і повертає True,
# ! якщо обидва слова починаються з однієї літери

def animal_crackers(text):
    wirdlist = text.split()
    # функція перевіряє, чи є перша літера першого слова (знаходиться у wirdlist[0][0])
    # рівною першій літері другого слова (знаходиться у wirdlist[1][0]).
    return wirdlist[0][0] == wirdlist[1][0]


print(animal_crackers('Levelheaded Llama'))


# ! задано два цілі числа, повертає True, якщо сума цілих чисел дорівнює 20 або
# ! якщо одне з цілих чисел дорівнює 20. Якщо ні, повертає False

def makes_twenty(n1, n2):
    if (n1 + n2) == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 0))


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


print(old_macdonald('macduck'))


# !MASTER YODA: Дано речення, поверніть речення зі словами, перевернутими
# ! master_yoda('I am home') --> 'home am I'
# ! master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda('home am I'))


def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


# print(almost_there(199))


def almost_there1(n):
    if 100 - n <= 10 or 200 - n <= 10:
        return True
    else:
        return False


# print(almost_there1(80))

# !Маючи список int, поверніть True, якщо масив десь містить 3 поруч із 3.

def find3(nums):
    for n in range(0, len(nums) - 1):
        if nums[n] == 3 and nums[n + 1] == 3:
            return True

    return False


print(find3([1, 3, 2, 3]))


# ? кожну парну літеру зробити великою
def myfunc(string):
    result = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
    return result


newstring = myfunc('Anthropomorphism')
print(newstring)


# ! БЛЕКДЖЕК: Дано три цілі числа від 1 до 11, якщо їх сума менша або дорівнює 21, поверніть їх суму.
# ! Якщо їх сума перевищує 21 і є одинадцять, зменшіть загальну суму на 10.
# ! Нарешті, якщо сума (навіть після коригування) перевищує 21, поверніть «BUST»

def blackjack(a, b, c):
    if (a + b + c) <= 21:
        return a + b + c
    elif (a + b + c) > 21 and a == 11 or b == 11 or c == 11:
        return (a + b + c) - 10
    else:
        return 'the sum more then 21'


print(blackjack(9, 9, 10))


# ! SUMMER OF '69:Повернути суму чисел у масиві, ігноруючи відрізки чисел,
# ! які починаються з 6 і продовжуються до наступної 9 (кожне число 6 буде наступати принаймні одне число 9).
# ! Повернути 0, якщо немає жодних чисел.

def summer_69(arr):
    total = 0
    for num in arr:
        if 6 <= num <= 9:
            continue
        else:
            total += num
    return total


print(summer_69([4, 5, 6, 7, 1, 8, 9]))
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))