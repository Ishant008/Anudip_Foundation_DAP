    
# Input from user
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times the interest is compounded per year: "))

#convert rate from percentage to decimal
rate = rate/ 100
    
# Compound Interest formula
amount = principal * (1 + rate / n) ** (n * time)

# Display the results
print("The compound interest is: ",amount)

