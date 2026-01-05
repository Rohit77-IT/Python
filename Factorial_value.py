def fact(n : int) -> int:
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

number = int(input("Enter the number: "))
if(number>=0):
    result = fact(number)
    print(f"The factorial is: {result}")
else:
    print("Enter a positive value")
    