str = input("Enter string: ")
counter = 0
letter ={}
for i in range(len(str)):
    for j in range(len(str)):
        if(str[i]==str[j]):
            counter= counter+1
            letter[str[i]] =counter

print(letter)