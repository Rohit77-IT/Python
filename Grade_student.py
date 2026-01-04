number = float(input("Enter your number to obtain the grade: "))
if(number>=90 and number<=100):
    print("Your grade is O\n")
elif(number>=80 and number<90):
    print("Your grade is E\n")
elif(number>=70 and number<80):
    print("Your grade is A\n")
elif(number>=60 and number<70):
    print("Your grade is B\n")
elif(number>=50 and number<60):
    print("Your grade is C\n")
elif(number>=40 and number<50):
    print("Your grade is D\n")
elif(number>=0 and number<40):
    print("Your grade is F\n")
else:
    print("Invalid number entered.\n")