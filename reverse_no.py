#input a number from the user
num=int(input("Enter a number : "))
#using loop to reverse that number
reverse=0
while num>0:
    reverse=reverse*10 + num%10
    num = num//10
#display the reverse number
print("The reverse of your given number is : ",reverse)  
    
