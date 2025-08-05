num=input("Enter of list of numbers(comma seperated)")
list=[int(i.strip()) for i in num.split(',') ]
ans=[]
for i in range(0,len(list)):
    if i%2!=0:
        ans.append(list[i])
print(ans)