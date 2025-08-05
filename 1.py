num=int(input("Enter a number :-"))
list=[]
if num>0:
    for i in range(num):
        list.append(i**2)
print(list)