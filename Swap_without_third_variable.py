a = int(input("Enter the numbera: "))
b = int(input("Enter the number b: "))
print(f"Before swapping a={a} and b={b}")
a = a + b
b = a - b
a = a - b
print(f"After swapping a={a} and b={b}")