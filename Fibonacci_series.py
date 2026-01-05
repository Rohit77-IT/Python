n = int(input("Enter the number of terms: "))
first = 1
second = 1
next = 0
print("Fibonacci series: ")
for i in range(0,n):
    print(first, end=" ")
    next = first+second
    first = second
    second = next

