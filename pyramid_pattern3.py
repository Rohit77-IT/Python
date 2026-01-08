rows = int(input("Enter the vaue of rows: "))
k = int(0)
for i in range(1,rows+1):
    for space in range(1,(rows-i) + 1):
        print("  ", end="")
    while(k!=2 * i - 1):
        print(" *", end="")
        k = k + 1
    print()
    k = 0