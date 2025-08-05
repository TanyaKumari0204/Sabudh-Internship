list=input("Enter the list of numbers(comma seperated):")
#converting string to list of nos.
numbers=[int(num.strip()) for num in list.split(',')]

ans=[]
for i in numbers:
    if i % 5==0:
        if i>500:
            break
        if i>150:
            continue
        
        ans.append(i)
print(ans)