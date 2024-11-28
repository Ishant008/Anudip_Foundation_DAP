#input five subjects marks from the user
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))
subject5 = float(input("Enter marks for Subject 5: "))

#calculate total marks
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

#calculate percentage
percentage = (total_marks / 500) * 100

# Output: Total marks and percentage
print("Total Marks = ",total_marks)
print("Percentage = ",percentage)
