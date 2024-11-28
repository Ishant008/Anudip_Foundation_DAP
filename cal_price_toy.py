#input product code and order amount from the user
product_code = int(input("Enter the product code (1 for Battery-based, 2 for Key-based, 3 for Electrical Charging-based): "))
order_amount = float(input("Enter the order amount: "))

#cal discounts based on the product code and order amount
if product_code == 1:  
    if order_amount > 1000:
        discount = 0.10  
    else:
        discount = 0.00 
elif product_code == 2:  
    if order_amount > 100:
        discount = 0.05  
    else:
        discount = 0.00  
elif product_code == 3:  
    if order_amount > 500:
        discount = 0.10  
    else:
        discount = 0.00  
else:
    print("Invalid product code entered.")
    discount = None

# Calculate the amount after discount

discount_amount = order_amount * discount
net_amount = order_amount - discount_amount

# Output the net amount
print("Net amount to pay: Rs.", net_amount)
