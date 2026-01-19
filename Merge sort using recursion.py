def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        mergesort(arr, left, mid)
        mergesort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def print_array(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()

m_input = input("Enter the size of array: ")
m = int(m_input)
arr = []
print("Enter integers (press Enter after each):")
for i in range(m):
    val = int(input())
    arr.append(val)
n = m
print("Original Array: ", end="")
print_array(arr, n)
mergesort(arr, 0, n - 1)
print("Sorted Array: ", end="")
print_array(arr, n)