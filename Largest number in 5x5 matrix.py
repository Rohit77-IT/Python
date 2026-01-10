matrix = []
print("Enter 25 elements for the 5x5 matrix: ")
for i in range(5):
    row = list(map(int, input(f"Enter row {i+1} (5 numbers separated by space): ").split()))
    matrix.append(row)
max_val = matrix[0][0]
for row in matrix:
    for element in row:
        if element > max_val:
            max_val = element
print(f"The largest number in the matrix is: {max_val}")