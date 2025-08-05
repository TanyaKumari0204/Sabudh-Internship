def factorial(n):
    fact=1
    if n>=0:
       for i in range(1,n+1):
           fact=fact*i
    return fact
num=int(input("enter the number:"))
print(factorial(num))
