
# Student Marks Analysis

# 1. Student marks list
marks = [98, 85, 45, 67, 89, 21, 35, 100, 76, 58,
         92, 40, 63, 88, 55, 72, 30, 95, 81, 65]

# 2. Basic analysis
total_students = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = sum(marks) / total_students

passed = 0
failed = 0
full_marks = 0

for mark in marks:
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if mark == 100:
        full_marks = full_marks + 1

pass_percentage = (passed / total_students) * 100

# 3. Sort marks in ascending and descending order
ascending_marks = sorted(marks)
descending_marks = sorted(marks, reverse=True)

# Highest and second lowest marks
highest = max(marks)
second_lowest = ascending_marks[1]

# 4. Check if all students passed
all_passed = all(mark >= 40 for mark in marks)

# 5. Grade distribution
grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_e = 0
grade_f = 0

for mark in marks:
    if mark >= 90:
        grade_a += 1
    elif mark >= 80:
        grade_b += 1
    elif mark >= 70:
        grade_c += 1
    elif mark >= 60:
        grade_d += 1
    elif mark >= 40:
        grade_e += 1
    else:
        grade_f += 1

# 6. Display output
print("Total Students:", total_students)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", round(average_marks, 2))
print("Passed:", passed)
print("Failed:", failed)
print("Pass Percentage:", round(pass_percentage, 2), "%")

print("Sorted Marks:", ascending_marks)
print("Descending Marks:", descending_marks)
print("Highest Marks:", highest)
print("Second Lowest Marks:", second_lowest)

print("All Students Passed:", all_passed)

print("Grade A:", grade_a, "Students")
print("Grade B:", grade_b, "Students")
print("Grade C:", grade_c, "Students")
print("Grade D:", grade_d, "Students")
print("Grade E:", grade_e, "Students")
print("Grade F:", grade_f, "Students")

# 7. Optional: Search for a student's marks
search_marks = int(input("Enter marks to search: "))

if search_marks in marks:
    print(search_marks, "is present in the list.")
else:
    print(search_marks, "is not present in the list.")
