myList = [2,1,3]
anotherList = [9,1,2,7,2,2,2]
myList.append(4)
# print(myList)

myList.sort()
# print(myList)

myList.sort(reverse=True)
# print(myList)

myList.append(anotherList)
# print(myList)

# print(anotherList.index(9))

# print(anotherList.count(2))

x = anotherList
# x[0] = 20
# print(anotherList)

secondList = [1,2,3,4]
secondList.insert(1,23)
# print(secondList)

F = [5,6,7,1,2,4,5,3]
# w = F+ secondList
# print(w)

# F = secondList+F
# print(F)
# print(F)
# F.clear()
# print(F)

# F.pop()
# print(F)

# F.remove(6)
# print(F)

# del F
# print(F)

# del F[1:3]
# print(F)

newList = [1,2,3,4, [5,6,7,8]]
print(newList)

newList.pop()
