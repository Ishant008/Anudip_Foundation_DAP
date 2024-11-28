#given string
string = "Welcome to python Training"

#a list of vowels
vowels=['a','e','i','o','u','A','E','I','O','U']
#count variable 
count=0

#run a loop which traverse each letter in the string and count the vowels
for char in string:
    if char in vowels:
        count=count+1
#display the total count of vowels
print("The total count of the vowels in the given string is : ",count)