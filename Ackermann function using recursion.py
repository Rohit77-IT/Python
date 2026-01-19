m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
def Ackermann(m,n):
    if(m==0):
        return n+1
    elif(n==0):
        return Ackermann(m-1,1)
    else:
        return Ackermann(m-1,Ackermann(m,n-1))
result = Ackermann(m, n)
print("The Ackermann value is:", result)