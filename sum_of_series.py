n = int(input("Enter the number of terms: "))
sum = float(0)
for i in range(1,n):
    sum += 1.0/i
print("Sum of the terms is: %f" %sum)