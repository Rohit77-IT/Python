def factorial(n):
    fact = 1.0
    for i in range(1, n + 1):
        fact *= i
    return fact
try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Invalid number")
    else:
        print(f"Factorial of {num} is {factorial(num):.0f}")
except ValueError:
    print("Please enter a valid integer.")