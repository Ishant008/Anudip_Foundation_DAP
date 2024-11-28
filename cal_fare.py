#input the distance traveled from the user
distance = float(input("Enter the distance traveled (in KM): "))

# Calculate fare based on the distance
if distance >= 1 and distance <= 50:
    fare = distance * 8  
elif distance > 50 and distance <= 100:
    fare = distance * 10 
else:
    fare = distance * 12  


#display the total fare
print("The total fare is:",fare)
