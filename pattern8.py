n=int(input("enter no of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    for k in range(0,n-i):
        print(" ",end=" ")
    for x in range(1,i+1):
        print("*",end="")
    print("\n",end="")


