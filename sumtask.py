myFile = open('file.txt')
myList = myFile.read().split(' ')
print(myList)

numList = [str(item).replace(',','').replace('.', '') for item in myList]
print(numList)

newList = []
for item in numList:
    if item.isdigit():
        num = int(item)
        if num > 1:
            #print(range(2,num))
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                newList.append(int(item))
print(newList)


