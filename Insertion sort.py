n = int(input("Enter the number of elements: "))
arr = [0] * n
print("Enter numbers (Press ENTER after each number): ")
for i in range(0, n):
    arr[i] = int(input())
order = int(input("Enter 1 for ascending , 2 for descending: "))
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and ((order == 1 and arr[j] > key) or (order == 2 and arr[j] < key)):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j+1] = key
print("Sorted numbers: ")
for i in range(0, n):
    print(arr[i], end=" ")
print()