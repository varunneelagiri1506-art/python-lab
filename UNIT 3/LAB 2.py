students = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter student marks: "))
    students[name] = marks
print("\n----- STUDENT GRADING SYSTEM -----")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    elif marks >= 40:
        grade = "E"
    else:
        grade = "Fail"
    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("------------------------")
