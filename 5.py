n=int(input("Enter a number :"))
digit=""
total=0
for i in range(n):
    digit+="2"
    total+=int(digit)
print(total)