def fibonacci(a, b, n):
    if n > 0:
        print(a, end=" ")
        fibonacci(b, a + b, n - 1)
num = int(input("Enter the number of terms: "))
if num <= 0:
    print("Please enter a valid number")
else:
    print("Fibonacci series:", end=" ")
    fibonacci(0, 1, num)
    print()