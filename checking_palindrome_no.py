#input a number from the user
num=int(input("Enter a number :"))
#using loop to reverse that number
num_copy=num
reverse=0
while num>0:
    reverse=reverse*10 + num%10
    num = num//10
#compare the original number with the reverse number to check it is palindrome or not
if reverse==num_copy:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")