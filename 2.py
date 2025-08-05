string=input("Enter a string: ")
sets=set()
result=[]
for i in string:
    if i not in sets:
        sets.add(i)#just to keep track of elements
        result.append(i)
print(''.join(result))