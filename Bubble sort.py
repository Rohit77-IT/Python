n = int(input("Enter the number of elements: "))
arr = [0] * n
print("Enter numbers (Press ENTER after each number): ")
for i in range(0, n):
    arr[i] = int(input())
order = int(input("Enter 1 for ascending , 2 for descending: "))
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if((order == 1 and arr[j] > arr[j+1]) or (order == 2 and arr[j] < arr[j+1])):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print("Sorted numbers: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()