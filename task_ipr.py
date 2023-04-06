# Считать из текстового файла числа, написанные через пробел, записать их в переменную типа list.
# Обработать этот список, выделив все простые числа в отдельный список.
# Вывести получившийся список простых чисел.

myFile = open('task.txt')

myList = myFile.read().split(' ')
print(myList)
numerList = []
for item in myList:
    item = item.replace(',','').replace('.','')
    if item.isdigit():
        num = int(item)
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                numerList.append(num)

print(numerList)






