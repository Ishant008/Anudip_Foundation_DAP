#input three numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

#check which number is the largest
if num1==num2 and num2==num3:
    print("all numbers are equal")
else:
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    #display the largest number
    print("The largest number is: ",largest)


