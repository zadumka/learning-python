myFile = open('file.txt')
myList = myFile.read().split(' ')
print(myList)

numList = [str(item).replace(',','').replace('.', '') for item in myList]
print(numList)


def evennumber(numList):
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
    return newList

newList = evennumber(numList)
print(newList)





# ! ------------------------------------------------
#myFile = open('file.txt')
#myList = myFile.read().split(' ')

#numList = [str(item).replace(',', '').replace('.', '') for item in myList]

#newList = []
#for item in numList:
#    if item.isdigit():
        #num = int(item)
        #if num > 1:

            #for i in range(2, num):
                #if num % i == 0:
                    #break
            #else:
                #newList.append(int(item))
#print(newList)
