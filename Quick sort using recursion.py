def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return i + 1
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

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
print("Original array: ", end="")
print_array(arr, n)
quicksort(arr, 0, n - 1)
print("Sorted array: ", end="")
print_array(arr, n)