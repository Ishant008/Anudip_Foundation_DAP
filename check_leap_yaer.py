#input year from the user
year = int(input("Enter a year: "))

#check leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year," is a leap year.")
else:
    print(year," is not a leap year.")
