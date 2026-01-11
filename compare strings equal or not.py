str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
isequal = True
if(len(str1) != len(str2)):
    isequal = False
else:
    i = 0
while(i<len(str1)):
        if str1[i] != str2[i]:
            isequal = False
            break
        i += 1
if(isequal):
    print("Both are same string.")
else:
    print("Both are different string")