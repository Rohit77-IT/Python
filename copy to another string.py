str_input = input("Enter a string: ")
str2_list = []
i = 0
try:
    while True:
        char = str_input[i]
        str2_list.append(char)
        i += 1
except IndexError:
    pass
str2 = "".join(str2_list)
print(f"Copied string: {str2}")