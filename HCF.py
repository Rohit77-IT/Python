a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
hcf = 1
for i in range(1,min(a,b)+1):
    if(a%i == 0 and b%i == 0):
        hcf = i
print(f"Hcf of {a} and {b} is {hcf}")