n = int(input("Enter the number of terms: "))
sum = float(0)
sign = int(-1)
odd = 1
for i in range(1, n+1):
    f = 1
    for j in range(1, odd+1):
        f = f * j
    sum += sign * (1.0/f)
    sign = -sign
    odd += 2
print("Summation of series: %f" % sum)