# Считать из текстового файла числа, написанные через пробел, записать их в переменную типа list.
# Обработать этот список, выделив все простые числа в отдельный список.
# Вывести получившийся список простых чисел.

myFile = open('task.txt')

myList = myFile.read().split(' ')

def even_list(myList):
    numberList = []
    for item in myList:
        item = item.replace(',','').replace('.','')
        if item.isdigit():
            num = int(item)
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    numberList.append(num)
    return numberList

numberList = even_list(myList)
print(numberList)



myFile = open('file.txt')
myList = myFile.read().split(' ')

numList = [str(item).replace(',', '').replace('.', '') for item in myList]

newList = []
for item in numList:
    if item.isdigit():
        num = int(item)
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                newList.append(num)
print(newList)




