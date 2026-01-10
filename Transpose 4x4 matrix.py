matrix = []
transpose = [[0 for _ in range(4)] for _ in range(4)]
print("Enter 16 elements for the 4x4 matrix:")
for i in range(4):
    row = []
    for j in range(4):
        element = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)
for i in range(4):
    for j in range(4):
        transpose[j][i] = matrix[i][j]
print("\nTranspose of the given matrix:")
for row in transpose:
    for element in row:
        print(element, end=" ")
    print()