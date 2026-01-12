is_palindrome = True
ster = input("Enter a string: ")
length = len(ster)
for i in range(length // 2):
    if ster[i] != ster[length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")