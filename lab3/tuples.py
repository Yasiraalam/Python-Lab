# ORDERED COLEECTION OF DATA ITEMS
t = (1,2,3,'hello','yasir')
print(t,type(t),'\n') #tuple
b = (3)
print(b,type(b),'\n') #class<Int>
c = (3,)
print(c,type(c),'\n')  #tuple
# slice
D = t[1:5:2]
print(D)

# change(typecast) tuple to list then back to tuple 
roll = (1,2,3,4,5,6,1,1,3)

print(roll,type(roll),'\n')
enrolled = list(roll)
print("typecast tuple ->roll to list-> enrolled \n",enrolled,type(enrolled),'\n')
enrolled.append(7)
print('after append 7 \n',enrolled)
enrolled.pop()
print('after pop \n',enrolled)
enrolled[1] = 8
roll = tuple(enrolled)
print('after assign 8 at index 1\n',roll)
# count fun used to check the frequecny of an element
print('frequency ',roll.count(1))   #3
print('frequency ',roll.count(3))   #2
r=roll.index(4)
print(r,type(r))  #this give the index where this value is located






