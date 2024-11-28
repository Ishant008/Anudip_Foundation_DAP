# Input Radius and height of the cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

#taking value of Pi in a variable
pi = 3.14159

# Calculate Curved Surface Area
curved_surface_area = 2 * pi * radius * height

# Calculate Total Surface Area 
total_surface_area = 2 * pi * radius * (radius + height)

# Calculate Volume of the Cylinder
volume = pi * radius * radius * height

#display Curved Surface Area, Total Surface Area, and Volume
print("Curved Surface Area (CSA):",curved_surface_area)
print("Total Surface Area (TSA):",total_surface_area)
print("Volume of the Cylinder:",volume)
