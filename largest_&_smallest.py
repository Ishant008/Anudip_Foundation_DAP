# Given list of numbers
numbers = [45, 12, 78, 34, 89, 2, 54]

#assume the first number is  the largest and also the smallest
largest = smallest = numbers[0]

# Loop through the list and compare each number
for num in numbers:
    if num > largest:
        largest = num
    
    if num < smallest:
        smallest = num

#display the largest and smallest numbers
print("Largest number:", largest)
print("Smallest number:", smallest)
