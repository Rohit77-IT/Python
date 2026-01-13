def factorial(n):
    if(n<=1):
        return 1.0
    else:
        return n * factorial (n-1)
try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Invalid number")
    else:
        print(f"Factorial of {num} is {factorial(num):.0f}")
except ValueError:
    print("Please enter a valid integer.")