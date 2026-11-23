attendance = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("\nEnter student name: ")
    status = input("Enter attendance (P/A): ").upper()
    if status == "P":
        attendance[name] = "Present"
    elif status == "A":
        attendance[name] = "Absent"
    else:
        print("Invalid input! Marked as Absent.")
        attendance[name] = "Absent"
print("\n----- ATTENDANCE REPORT -----")
present = 0
absent = 0
for name, status in attendance.items():
    print(name, ":", status)
    if status == "Present":
        present += 1
    else:
        absent += 1
print("\nTotal Students:", n)
print("Total Present:", present)
print("Total Absent:", absent)
print("Attendance Percentage:", (present / n) * 100, "%")
