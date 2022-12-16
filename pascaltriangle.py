def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def nCr(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))
n=int(input("enter no of rows"))
for i in range(0,n):
    for j in range(0,i+1):
        print(nCr(i,j),end=" ")
    print("\n",end="")
