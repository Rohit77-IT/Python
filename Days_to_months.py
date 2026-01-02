days = int(input("Enter the number of days: "))
months = days // 30
remaining_days =  days % 30
print(f"{days} is same as {months} months and {remaining_days} days")