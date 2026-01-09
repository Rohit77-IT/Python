n = int(input("Enter the number of elements: "))
arr = [0] * n
print("Enter numbers (Press ENTER after each number): ")
for i in range(0, n):
    arr[i] = int(input())
order = int(input("Enter 1 for ascending , 2 for descending: "))
for i in range(0, n-1):
    x = i
    for j in range(i+1, n):
        if((order == 1 and arr[j] < arr[x]) or (order == 2 and arr[j] > arr[x])):
            x = j
    if(x!=i):
        temp = arr[x]
        arr[x] = arr[i]
        arr[i] = temp
print("Sorted numbers: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()