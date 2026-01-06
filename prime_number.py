n = int(input("Enter the number you want to check: "))
ctr = 0
for i in range(1,n+1):
    if(n%i==0):
        ctr += 1
if(ctr==2):
    print("The number is a prime number")
else:
    print("The number is not a prime number")