# Step 1: Get user input
name = input("Enter your name: ")
mark1 = float(input("Enter mark for subject 1: "))
mark2 = float(input("Enter mark for subject 2: "))
mark3 = float(input("Enter mark for subject 3: "))

# Step 2: Calculate the average
average = (mark1 + mark2 + mark3) / 3

# Step 3: Determine the grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Step 4 (Bonus): Pass or Fail
if average >= 50:
    status = "PASS"
else:
    status = "FAIL"

# Output the result
print("\n=== Grade Report ===")
print("Student Name:", name)
print("Average Mark:", round(average, 2))
print("Grade:", grade)
print("Status:", status)
