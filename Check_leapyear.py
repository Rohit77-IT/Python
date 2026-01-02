year = int(input("Enter the year you want to check: "))
if (year%400==0) or (year%100!=0 and year%4==0):
    print("%d is a leap year" % year)
else:
    print("%d is not a leap year" % year)