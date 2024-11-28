#input a number from the user
num=int(input("Enter a number : "))
#calculate the factorial using while loop
factorial=1
i=num
while i>0:
    factorial=factorial*i
    i=i-1
#display the factorial of that number to the user
print("The factorial of given number is : ",factorial)