def remove_the_thirds(numList):
   newList = []
   for i in range(len(numList)):
       if (i + 1) % 3 != 0:
           newList.append(numList[i])
   return newList

list1 = [3,6,6,3,7,2,0,1,5,4]
print(remove_the_thirds(list1))