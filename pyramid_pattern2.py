n = int(input("Enter the vaue of n: "))
for i in range(1,n+1):
    for j in range(1,(n-i) + 1):
        print("  ", end="")
    a = i
    for j in range(1,i+1):
        print("%d "%a, end="")
        a = a + 1
    a = a - 2
    for j in range(1,i):
        print("%d "%a, end="")
        a = a - 1
    print()