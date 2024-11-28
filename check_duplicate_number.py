#Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 3, 2, 8, 9, 1]

#empty list to store only duplicate numbers
duplicate=[]

#run a loop which traverse the numbers in the list and find duplicate
for i in range(0,len(numbers)):
    if numbers[i] not in duplicate:
        for j in range(i+1,len(numbers)):
            if numbers[i]==numbers[j]:
                duplicate.append(numbers[i])

#display the list of duplicates
print("The duplicate numbers are : " ,duplicate)
       
    
