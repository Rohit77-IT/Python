str_input = input("Enter a string: ")
length = 0
try:
    while True:
        c = str_input[length] 
        length += 1
except IndexError:
    pass
print(f"Length of the string: {length}")