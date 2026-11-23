import csv

try:
    n = int(input("Enter number of employees: "))

    if n < 0:
        raise ValueError("Number of employees cannot be negative.")

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID",
            "Name",
            "Basic",
            "Allowance",
            "Deduction",
            "Net Salary"
        ])

        for i in range(n):
            print(f"\nEnter details for employee {i + 1}")
            emp_id = input("Employee ID: ")
            name = input("Employee Name: ")
            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))

            net_salary = basic + allowance - deduction

            writer.writerow([
                emp_id,
                name,
                basic,
                allowance,
                deduction,
                net_salary
            ])

    print("Payroll data saved to payroll.csv.")

except ValueError:
    print("Invalid input. Enter a whole number for employee count and numeric values for salaries.")

except Exception as e:
    print(f"Error: {e}")