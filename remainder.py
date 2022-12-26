num=int(input("enter number"))
divisor=int(input("enter divisor"))
def getRemainder(num, divisor):
    return (num - divisor * (num // divisor))
print(getRemainder(num,divisor))
