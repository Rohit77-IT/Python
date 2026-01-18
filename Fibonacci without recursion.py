n = int(input("Enter the number of terms: "))
a = 0
b = 1
next = 0
print("Fibonacci series: ")
for i in range(0,n):
    print(a, end=" ")
    next = a+b
    a = b
    b = next