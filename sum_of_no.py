#taking a variable to store the sum
sum = 0
# Start an loop which will break if user input a zero
while True:
#input a number from the user
    num = int(input("Enter a number (0 to stop): "))
#if the user enters 0 then break the loop
    if num == 0:
        break
    sum = sum + num

#display the sum of all entered numbers
print("The sum of all the numbers is:",sum)
