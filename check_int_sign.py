#input a number from the user
num = int(input("Enter a number: "))

#check if the number is positive, negative, or zero
if num > 0:
    print(num," is a positive number.")
elif num < 0:
    print(num," is a negative number.")
else:
    print("Your given number is zero is zero.")
